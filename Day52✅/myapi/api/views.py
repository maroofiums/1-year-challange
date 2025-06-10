from rest_framework.response import Response
from .serializers import Transaction_Serializers
from .models import Transactions
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def get_transations(request):
    queryset = Transactions.objects.all()
    serializer = Transaction_Serializers(queryset,many=True)
    return Response({
        "data":serializer.data,
    })