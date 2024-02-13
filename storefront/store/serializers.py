from rest_framework import serializers
from decimal import Decimal
from store.models import Product


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    Price = serializers.DecimalField(
        max_digits=6, decimal_places=2, source='price')
    price_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self, p: Product):
        return p.price * Decimal(1.78)
