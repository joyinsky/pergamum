import os
import datetime
import pymongo
from pergamum.bibloi.models import *
from dateutil.parser import parse
from django.core.files import File

TEXT_TYPES = ['txt', 'rtf', 'doc', 'pdf', 'htm', 'docx', 'pps', 'pptx','xls']


db = pymongo.MongoClient('mongodb://localhost:27017/')
articulos = db.archivo.articulos
data = [n for n in articulos.find({}, {"_id": 1, "metadata.title": 1, "metadata.Creation-Date": 1, "content": 1, "path": 1, "ext": 1, "folder": 1, "filename": 1, "created": 1})]
datalen = len(data)


for count, elem in enumerate(data):
    print(count, "/", datalen)
    if elem.get('ext') in TEXT_TYPES:
        with open(elem['path'], 'rb') as file_:
            art = Article()
            title = elem.get('metadata', {}).get('title', '') or elem.get('filename', '')
            if type(title) == list and title:
                title = title[0]
            art.name = title.replace('\x00', '')
            date = elem.get('metadata', {}).get('Creation-Date')
            if date:
                if isinstance(date, list):
                    date = max(date)
                art.date = parse(date).date()
            else:
                art.date = datetime.datetime.fromtimestamp(os.path.getctime(elem['path'])).date()
            if elem.get('content'):
                art.content = elem.get('content', '').strip()
            else:
                art.content = ''
            if elem.get('folder'):
                folders = elem.get('folder').split('/')
                current = None
                for folder in folders:
                    f, _ = Folder.objects.get_or_create(name=folder, parent=current, defaults={'order': 1})
                    current = f
                art.folder = current
            art.uid = str(elem.get('_id'))
            djf = File(file_)
            path = os.path.join(*elem['path'].split('/')[1:])
            art.source_file.save(path, djf, save=True)
            art.save()
