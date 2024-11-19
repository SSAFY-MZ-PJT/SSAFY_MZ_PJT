from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=255)
    photo_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=255)
    photo_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    genres = models.ManyToManyField(Genre, related_name="movies")  # M:N 관계
    release_date = models.DateField(blank=True, null=True)
    poster_image_url = models.URLField(blank=True, null=True)
    plot = models.TextField(blank=True, null=True)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, related_name="movies")
    actors = models.ManyToManyField(Actor, related_name="movies")  # M:N 관계

    def __str__(self):
        return self.title
