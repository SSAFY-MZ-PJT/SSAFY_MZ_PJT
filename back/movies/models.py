# movies/models.py

from django.db import models
from django.conf import settings

class Director(models.Model):
    tmdb_id = models.IntegerField(unique=True, null=True, blank=True)  # TMDB ID 추가
    name = models.CharField(max_length=255)
    photo_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Actor(models.Model):
    tmdb_id = models.IntegerField(unique=True, null=True, blank=True)  # TMDB ID 추가
    name = models.CharField(max_length=255)
    photo_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_movies", blank=True)
    tmdb_id = models.IntegerField(unique=True, null=True, blank=True)  # TMDB ID 추가
    title = models.CharField(max_length=255)
    genres = models.ManyToManyField(Genre, related_name="movies")  # M:N 관계
    release_date = models.DateField(blank=True, null=True)
    poster_image_url = models.URLField(blank=True, null=True)
    plot = models.TextField(blank=True, null=True)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, related_name="movies")
    rating = models.FloatField(default=0, null=True, blank=True)  # 영화 평점 추가
    actors = models.ManyToManyField(Actor, related_name="movies")  # M:N 관계
    is_now_playing = models.BooleanField(default=False)  # 현재 상영 중인지
    is_popular = models.BooleanField(default=False)      # 인기 영화인지

    def __str__(self):
        return self.title
