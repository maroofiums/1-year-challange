from django.urls import path
from . import views

urlpatterns = [
    path('slow/', views.slow_view, name='slow'),
    path('fast/', views.fast_view, name='fast'),
]
