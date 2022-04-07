from distutils.command.upload import upload
from unicodedata import category
from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=230,default='',null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    image = models.ImageField(upload_to = "products/")

    @staticmethod
    def get_all_products():
        return Product.objects.all()