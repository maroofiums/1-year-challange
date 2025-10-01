from django.urls import path,include
from .views import BookViewSeter
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"book",BookViewSeter)

urlpatterns = [
    path("",include(router.urls)),
]
