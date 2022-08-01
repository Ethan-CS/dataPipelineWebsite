from django.db import models


# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=100)
    distance = models.FloatField(max_length=100)
    location = models.CharField(max_length=100)
    kind = models.CharField(max_length=100)
