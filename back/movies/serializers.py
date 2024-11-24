# movies/serializers.py

from rest_framework import serializers
from movies.models import Movie, Director, Actor, Genre
from shared.serializers import SimpleUserSerializer, SimpleReviewSerializer


class DirectorSerializer(serializers.ModelSerializer):
    movies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  # 역참조: 감독이 연출한 영화

    class Meta:
        model = Director
        fields = ('id', 'name', 'tmdb_id', 'photo_url', 'movies')


class ActorSerializer(serializers.ModelSerializer):
    movies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  # 역참조: 배우가 출연한 영화

    class Meta:
        model = Actor
        fields = ('id', 'name', 'tmdb_id', 'photo_url', 'movies')


class GenreSerializer(serializers.ModelSerializer):
    movies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  # 역참조: 장르와 연결된 영화

    class Meta:
        model = Genre
        fields = ('id', 'name', 'movies')


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    actors = ActorSerializer(many=True)
    genres = GenreSerializer(many=True)

    # 역참조 관계
    likes = SimpleUserSerializer(many=True, read_only=True)
    reviews = SimpleReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

