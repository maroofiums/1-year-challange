from django.urls import path
from .views import blog_list,blog_create,blog_detail,blog_update,blog_delete

urlpatterns = [
    path('blog/',blog_list,name='blog_list'),
    path('blog/<int:pk>/',blog_detail,name='blog_list'),
    path('blog/create/',blog_create,name='blog_list'),
    path('blog/update/<int:pk>/',blog_update,name='blog_list'),
    path('blog/delete/<int:pk>/',blog_delete,name='blog_list'),
]