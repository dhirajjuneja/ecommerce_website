from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view()),
    path('product', ProductView.as_view())
]