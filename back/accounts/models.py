# accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Genre


class User(AbstractUser):
    nickname = models.CharField(max_length=100, blank=True)
    profile_image = models.ImageField(upload_to='profile/', null=True, blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followings', blank=True)
    favorite_genres = models.ManyToManyField(Genre, related_name="users", blank=True)

    def __str__(self):
        return self.username
    
# mysql -u root -p
# DROP DATABASE cinerium;
# CREATE DATABASE cinerium CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

# mysqldump -u root -p --default-character-set=utf8mb4 cinerium > data.sql
# mysql -u root -p cinerium < data.sql