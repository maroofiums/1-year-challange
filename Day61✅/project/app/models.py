from django.db import models

# Create your models here.

class Receipes(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ImageField(upload_to="receipes_image")

    def __str__(self):
        return self.title