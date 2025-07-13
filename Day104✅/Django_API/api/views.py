from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class ProtectedAPI(APIView):
    permission_class = [IsAuthenticated]
    
    def get(self, request):
        return Response({"message":f"Hello {request.user.username}, you are logged in!"})
    
    