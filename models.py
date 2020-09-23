from django.db import models

class Item(models.Model):
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=25)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    
