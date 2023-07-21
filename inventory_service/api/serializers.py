from rest_framework import serializers

from .models import Inventory
class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['title', 'sku', 'qty']