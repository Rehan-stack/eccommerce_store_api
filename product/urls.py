from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('list', List_product.as_view()),
    path('list/<int:pk>',list_product_details.as_view()),
    path('create/<int:pk>',create_product.as_view()),
]
