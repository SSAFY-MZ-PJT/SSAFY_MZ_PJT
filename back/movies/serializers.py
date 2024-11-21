# movies/serializers.py

from rest_framework import serializers
from .models import Movie, Director, Actor, Genre
from reviews.models import Review

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name', 'photo_url']


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name', 'photo_url']


class ReviewListSerializer(serializers.ModelSerializer):
    """
    영화에 연결된 리뷰 간략한 정보를 포함하는 Serializer
    """
    class Meta:
        model = Review
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'user']  # 필요한 필드만 포함


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer(read_only=True)
    actors = ActorSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

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
            'rating',
            'adult',
            'budget',
            'revenue',
            'popularity',
            'runtime',
            'tagline',
            'vote_count',
            'is_now_playing',
            'is_popular',
        ]


