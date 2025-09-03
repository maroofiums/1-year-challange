from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializers

class BookViewSeter(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
