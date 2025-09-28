from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import BookViewSeter

router = DefaultRouter()
router.register(r"books",BookViewSeter)

urlpatterns = [
    path("",include(router.urls))
]
