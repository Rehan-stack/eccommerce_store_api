from rest_framework import serializers
from .models import *




class Product_serializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['__all__']





class Product_detail_serializer(serializers.ModelSerializer):
    class Meta:
        model = Product_details
        fields = ['__all__']