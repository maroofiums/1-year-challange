from django.urls import path
from .views import get_notes, create_post, update_note, delete_note

urlpatterns = [
    path("notes/", get_notes, name="get-notes"),
    path("notes/create/", create_post, name="create-note"),
    path("notes/update/<str:pk>/", update_note, name="update-note"),
    path("notes/delete/<str:pk>/", delete_note, name="delete-note"),
]
