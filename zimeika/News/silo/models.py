from django.db import models

# Create your models here.



class NewsInfo(models.Model):
    Title = models.CharField(max_length=100)
    Url = models.CharField(max_length=100)
    Author = models.CharField(max_length=20)
    Time = models.CharField(max_length=50)
    Reading = models.CharField(max_length=20)
    Comment = models.CharField(max_length=20)
    Classify = models.CharField(max_length=20)
    Content = models.CharField(max_length=10000)