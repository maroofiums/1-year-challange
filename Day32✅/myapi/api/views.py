from django.shortcuts import render
from rest_framework.response import Response
from .serializers import TransactionSerializer
from rest_framework.decorators import api_view
from .models import Transaction
# Create your views here.

@api_view(['GET'])
def get_transaction(request):
    queryset= Transaction.objects.all()
    serializer = TransactionSerializer(queryset,many=True)
    return Response({
        "data":serializer.data
    })