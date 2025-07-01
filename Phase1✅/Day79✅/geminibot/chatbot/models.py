from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)  # Associate with user
    user_message = models.TextField()
    bot_reply = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"[{self.timestamp:%Y-%m-%d %H:%M}] {self.user.username}: {self.user_message[:30]}..."

    class Meta:
        ordering = ['-timestamp']  # Latest messages first