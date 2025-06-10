from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializer
from .models import Post

# Create your views here.

@api_view(['GET'])
def see_post(request):
    queryset = Post.objects.all()
    serializer = PostSerializer(queryset,many=True)
    return Response(
        {
            "data":serializer.data
        }
    )