from django.db import models

class Unit(models.Model):
    nickname = models.CharField(max_length=40)
    address = models.CharField(max_length=120)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
