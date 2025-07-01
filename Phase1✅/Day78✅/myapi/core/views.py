# core/views.py
from rest_framework import generics, permissions
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def profile(request):
    return Response({
        "message": "Hello, " + request.user.username
    })
