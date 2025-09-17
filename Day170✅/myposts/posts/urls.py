from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import PostViewSeter

router = DefaultRouter()
router.register(r"posts",PostViewSeter)

urlpatterns = [
    path('',include(router.urls))
]
