from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Chat(models.Model):
    chat_id = models.CharField(max_length=64, null=False, blank=False, unique=True)
    name = models.CharField(max_length=1024, null=False, blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owned_chats")
    members = models.ManyToManyField(User, related_name="membered_chats")


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(null=False, blank=False)
