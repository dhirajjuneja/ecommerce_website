from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    default_user = models.OneToOneField(User, null=True, blank=False,on_delete=models.CASCADE)
    name = models.CharField('Name', max_length=120, null=True,blank=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    customer = models.ForeignKey(Customer, null=True ,on_delete=models.CASCADE)
    name = models.CharField('Product Name' ,max_length=120, blank=False,null=True)
    image = models.ImageField( blank=True, upload_to='images/')
    price = models.IntegerField('Price', blank=False,null=True)
    description = models.TextField('Description', blank=True,null=True)

    def __str__(self):
        return self.name