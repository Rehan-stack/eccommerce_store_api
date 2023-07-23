from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.validators import ValidationError
# Create your views here.
 
class List_product(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = Product_serializer

 
class list_product_details(ListAPIView):
    serializer_class = Product_detail_serializer
      
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Product_details.objects.filter(product = pk)
    


class create_product(CreateAPIView):
    serializer_class = Product_serializer

    def perform_create(self, serializer):
        pk = self.kwargs['pk']

        query = Product.objects.get(pk=pk)
        

        add_product = Product_details.objects.filter(query=query)
        if add_product.exists():
            raise ValidationError('product already exists, try to add new product.')
        else:
            query.save()
        return Response(query.data)