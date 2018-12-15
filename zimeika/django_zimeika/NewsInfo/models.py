from django.db import models
from mongoengine import *
# Create your models here.
connect('ZiMeiKa',host='127.0.0.1',port=27017)
class ZiMeiKaInfo(Document):
    Title = StringField()
    Url = StringField()
    Author = StringField()
    Time = StringField()
    Reading = StringField()
    Comment = StringField()
    Classify = StringField()
    Content = StringField()
    meta = {'collection':'NewsTitle'}

