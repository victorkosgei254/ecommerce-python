from django.db import models

# Create your models here.
class Order(models.Model):

    product_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    cart_id = models.CharField(max_length=255)
    

