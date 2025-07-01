from .views import *
from django.urls import path

urlpatterns = [
    path('', get_transations),
]