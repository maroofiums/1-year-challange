from django.db import models

# Create your models here.

class Post_model(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = '__all__'

    def __str__(self):
        return self.title