from django.shortcuts import render
from django.views.generic import *
from .models import *

# Create your views here.

def home(request):
    customer = Customer.objects.all()
    product = Product.objects.all()
    context = {'customer':customer,'product': product}
    return render(request, 'ecom_app/home.html', context)



class ProductView(ListView):
    model = Product
    template_name = 'ecom_app/productd.html'
