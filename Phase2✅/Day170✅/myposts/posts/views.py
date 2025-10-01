from rest_framework import viewsets
from .models import Posts
from .serializers import PostSerializers

class PostViewSeter(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializers
    