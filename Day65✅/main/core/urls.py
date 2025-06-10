from django.urls import path
from .views import post_view,update_view,delete_view
urlpatterns = [
    path('',post_view,name="post"),
    path('delete/<int:id>',delete_view,name="delete"),
    path('update/<int:id>',update_view,name="update"),
]
