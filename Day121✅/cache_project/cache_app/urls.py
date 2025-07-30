from django.urls import path
from .views import home_view, data_view

urlpatterns = [
    path('', home_view, name='home'),
    path('data/', data_view, name='data'),
]
