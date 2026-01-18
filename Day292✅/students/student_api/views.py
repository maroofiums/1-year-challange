from .serializers import Student_Serializers
from rest_framework import viewsets
from .models import StudentModel

class Student_ViewSets(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = Student_Serializers
    