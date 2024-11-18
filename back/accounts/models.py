from django.contrib.auth.models import AbstractUser
from django.db import models
from movies.models import Genre

class User(AbstractUser):
    email = models.EmailField(unique=True)
    interests = models.TextField(blank=True, null=True)
    favorite_genres = models.ManyToManyField(Genre, related_name="users", blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)

    def __str__(self):
        return self.username

class Chat(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chats")

class ChatMessage(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)