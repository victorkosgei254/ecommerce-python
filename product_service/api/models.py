from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.CharField(max_length=255)
