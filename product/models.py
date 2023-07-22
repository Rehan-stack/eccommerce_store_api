from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    brand_name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Product_details(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.IntegerField(validators=[MaxValueValidator(50)])
    instock = models.BooleanField(default=True)

    def __str__(self):
        return str(self.product.name)
    


    