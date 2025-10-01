from django.urls import path
from . import views

urlpatterns = [
    path("expensive/", views.expensive_view),
    path("fast/", views.fast_view),
]
