from .views import chat_view
from django.urls import path

urlpatterns = [
    path("", chat_view, name="chat_view"),
]
