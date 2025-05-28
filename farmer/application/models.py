from django.db import models
from django.db import models

class summer(models.Model):
    name = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    expiry_date = models.DateField()
    manufacturing_date = models.DateField()


class monsoon(models.Model):
    name = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    expiry_date = models.DateField()
    manufacturing_date = models.DateField()
