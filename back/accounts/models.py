# accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Genre


class User(AbstractUser):
    profile_image = models.ImageField(upload_to='profile/', null=True, blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followings', blank=True)
    introduce = models.TextField(blank=True, default='')
    favorite_genres = models.ManyToManyField(Genre, related_name="users", blank=True)

    def __str__(self):
        return self.username
