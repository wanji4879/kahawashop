from django.db import models
from django.contrib import admin


class Kahawaapp(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.PositiveIntegerField()
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.name


  