from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorModel
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = OrderModel
        fields = '__all__'