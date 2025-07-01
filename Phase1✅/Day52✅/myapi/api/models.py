from django.db import models

# Create your models here.

class Transactions(models.Model):
    title = models.CharField(max_length=100)
    amount = models.FloatField()
    transaction_type = models.CharField(max_length=100,choices=(("CREDIT","CREDIT"),("DEBIT","DEBIT")))
    def save(self,*args, **kwargs):
        self.amount = self.amount * -1
        return super().save(*args, **kwargs)