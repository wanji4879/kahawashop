from django.db import models


class Kahawaapp(models.Model):
  name= models.CharField(max_length=255)
  price = models.FloatField()
  Quantity = models.IntegerField()
  image =models.CharField(max_length=2083)

  