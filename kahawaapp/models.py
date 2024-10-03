from django.db import models

class Kahawaapp(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='coffee_photos/')

    def _str_(self):
        return self.name 
