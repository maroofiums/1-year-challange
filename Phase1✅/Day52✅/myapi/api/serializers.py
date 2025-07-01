from rest_framework import serializers
from .models import Transactions

class Transaction_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = "__all__"
