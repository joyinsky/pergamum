import pymongo
from pergamum.bibloi.models import *
from dateutil.parser import parse
from django.core.files import File


db = pymongo.MongoClient('mongodb://localhost:27017/')
articulos = db.archivo.articulos
data = [n for n in articulos.find({}, {"_id": 1, "metadata.title": 1, "metadata.Creation-Date": 1, "content": 1, "path": 1, "ext": 1, "folder": 1, "filename": 1, "created": 1})]

for count, elem in enumerate(data):
    print(count, elem)
    with open(elem['path']) as f:
        art = Article()
        art.name = elem['metadata']['title']
        art.date = parse(elem['metadata']['Creation-Date']).date()
        art.content = elem['content']
        if elem.get('folder'):
            folders = elem.get('folder').split('/')
            current = None
            for folder in folders:
                f = Folder.objects.get_or_create(name=folder, parent=current)
                current = f
            art.folder = current
        art.uid = str(elem.get('_id'))
        djf = File(f)
        art.source_file.save(elem['path'], djf, save=True)
        art.save()
