from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Post_model
from .serializers import Post_serializer

# Create your views here.

@api_view(['GET','POST'])
def post_view(request):
    if request.method == 'GET':
        posts = Post_model.objects.all()
        serializer = Post_serializer(posts,many =True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = Post_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def post_detail(request,pk):
    try:
        post = Post_model.objects.get(pk=pk)
    except Post_model.DoesNotExist:
        return Response({'error':'Post not found'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Post_serializer(post)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = Post_serializer(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        post.delete()
        return Response({'message': 'Post deleted'}, status=status.HTTP_204_NO_CONTENT)
