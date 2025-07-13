from django.urls import path
from .views import ProtectedAPI
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/protected/', ProtectedAPI.as_view()),
]
