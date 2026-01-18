from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Student_Serializers

router = DefaultRouter()
router.register(r'students', Student_Serializers)

urlpatterns = [
    path('', include(router.urls)),
]
