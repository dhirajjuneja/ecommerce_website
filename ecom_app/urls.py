from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('product/<str:pk_test>/', ProductView.as_view(), name='product'),
    path('customer', ProductView.as_view(), name='customer'),
]