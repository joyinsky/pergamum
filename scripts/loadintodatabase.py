import pymongo
from pergamum.bibloi.models import *
from dateutil.parser import parse
from django.core.files import File
import os
TEXT_TYPES = ['txt', 'rtf', 'doc', 'pdf', 'htm', 'docx', 'pps', 'pptx','xls']


db = pymongo.MongoClient('mongodb://localhost:27017/')
articulos = db.archivo.articulos
data = [n for n in articulos.find({}, {"_id": 1, "metadata.title": 1, "metadata.Creation-Date": 1, "content": 1, "path": 1, "ext": 1, "folder": 1, "filename": 1, "created": 1})]

for count, elem in enumerate(data):
    print(count, elem)
    if elem.get('ext') in TEXT_TYPES:
        with open(elem['path'], 'rb') as file_:
            art = Article()
            art.name = elem['metadata']['title']
            art.date = parse(elem['metadata']['Creation-Date']).date()
            art.content = elem['content']
            if elem.get('folder'):
                folders = elem.get('folder').split('/')
                current = None
                for folder in folders:
                    f, _ = Folder.objects.get_or_create(name=folder, parent=current, defaults={'order': 1})
                    current = f
                art.folder = current
            art.uid = str(elem.get('_id'))
            djf = File(file_)
            path = os.path.join(elem['path'].split('/')[1:])
            art.source_file.save(elem['path'], djf, save=True)
            art.save()
