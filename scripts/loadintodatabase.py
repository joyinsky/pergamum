# coding: utf-8
import pymongo
from pergamum.bibloi.models import *
from dateutil.parser import parse

db = pymongo.MongoClient('mongodb://localhost:27017/')
articulos = db.archivo.articulos
data = [n for n in articulos.find({}, {"_id": 1, "metadata.title": 1, "metadata.Creation-Date": 1, "content": 1, "path": 1, "ext": 1, "folder": 1, "filename": 1, "created": 1})]

for elem in data:
    art = Article()
    art.name = elem['metadata']['title']
    art.date = elem['']
