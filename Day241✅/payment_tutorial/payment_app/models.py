from django.db import models

class Payment(models.Model):
    amount = models.IntegerField()
    stripe_payment_intent = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"${self.amount / 100} - {self.stripe_payment_intent}"
