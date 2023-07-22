from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import *
from .models import *
from rest_framework.response import Response
# Create your views here.

class List_product(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = Product_serializer


class list_product_details(ListAPIView):
    serializer_class = Product_detail_serializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Product_details.objects.filter(product = pk)
    


