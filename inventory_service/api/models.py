from django.db import models

# Create your models here.
class Inventory(models.Model):
    inv_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    sku = models.CharField(max_length=255)
    qty = models.IntegerField()