from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_value=150)
    email = models.EmailField()

    def __str__(self):
        return self.name