from rest_framework import serializers
from .models import Post_model

class Post_serializer(serializers.ModelSerializer):
    class Meta:
        model = Post_model
        fields = '__all__'