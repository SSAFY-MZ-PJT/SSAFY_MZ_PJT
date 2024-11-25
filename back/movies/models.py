# movies/models.py

from django.db import models
from django.conf import settings

class Director(models.Model):
    tmdb_id = models.IntegerField(unique=True, null=True, blank=True)
    name = models.CharField(max_length=255)
    photo_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Actor(models.Model):
    tmdb_id = models.IntegerField(unique=True, null=True, blank=True)
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
    actors = models.ManyToManyField(Actor, related_name="movies")
    genres = models.ManyToManyField(Genre, related_name="movies")
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, related_name="movies")
    tmdb_id = models.IntegerField(unique=True, null=True, blank=True)
    title = models.CharField(max_length=255)
    release_date = models.DateField(null=True, blank=True)
    poster_image_url = models.URLField(null=True, blank=True)
    plot = models.TextField(blank=True, default="")
    rating = models.FloatField(default=0)
    adult = models.BooleanField(default=False)
    budget = models.IntegerField(default=0)
    revenue = models.IntegerField(default=0)
    popularity = models.FloatField(default=0)
    runtime = models.IntegerField(default=0)
    tagline = models.TextField(default="", blank=True)
    vote_count = models.IntegerField(default=0)
    trailer_url = models.URLField(null=True, blank=True)
    is_now_playing = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)

    def __str__(self):
        return self.title


