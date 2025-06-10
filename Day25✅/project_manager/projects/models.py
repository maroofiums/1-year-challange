from django.db import models

# Create your models here.

class Project(models.Model):
    STATUS_CHOICES = [
        ('pending','Pending'),
        ('in_progress','In Progress'),
        ('completed','Completed'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')
    dateline = models.DateField()

    def __str__(self):
        return self.title
    