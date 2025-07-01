from django.db import models

# Create your models here.

class Shop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=True)
    images = models.ImageField(upload_to="product",null=True,blank=True)
    def __str__(self):
        return self.name