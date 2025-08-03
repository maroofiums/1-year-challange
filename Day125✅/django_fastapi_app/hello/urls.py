from django.urls import path
from . import views

app_name = 'hello'

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('hello/<str:name>/', views.hello_name, name='hello_name'),
] 