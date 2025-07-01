from django.urls import path
from .views import see_post
urlpatterns = [
    path('api/',see_post)
]