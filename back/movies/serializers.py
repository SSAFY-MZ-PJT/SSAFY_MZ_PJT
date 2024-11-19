# movies/serializers.py

from rest_framework import serializers
from .models import Movie, Director, Actor, Genre

# Genre Serializer
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


# Director Serializer
class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name', 'photo_url']


# Actor Serializer
class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name', 'photo_url']


# Movie Serializer
class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)  # Nested Serializer for genres
    director = DirectorSerializer(read_only=True)       # Nested Serializer for director
    actors = ActorSerializer(many=True, read_only=True) # Nested Serializer for actors

    class Meta:
        model = Movie
        fields = [
            'id', 
            'title', 
            'genres', 
            'release_date', 
            'poster_image_url', 
            'plot', 
            'director', 
            'actors', 
            'is_now_playing', 
            'is_popular'
        ]
