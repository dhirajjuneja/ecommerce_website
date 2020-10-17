from django.shortcuts import render
from django.views.generic import *
from .models import *

# Create your views here.

class HomeView(ListView):
    model = Customer
    template_name = 'ecom_app/home.html'

class ProductView(ListView):
    model = Product
    template_name = 'ecom_app/products.html'
