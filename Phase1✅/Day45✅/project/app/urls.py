from django.urls import path
from .views import *

urlpatterns = [
    path('', add_post, name='receipes'),
    path('delete/<int:id>/', delete, name='delete'),
]
