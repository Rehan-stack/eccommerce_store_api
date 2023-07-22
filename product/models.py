from django.db import models

# Create your models here.


class Product(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    brand_name = models.CharField(max_length=50)

    def __str__(self):
        return self.image
    

class Product_details(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.IntegerField(max_length=50)
    instock = models.BooleanField(default=True)

    def __str__(self):
        return self.product.name
    

    
    