# shared/serializers.py

from rest_framework import serializers
from accounts.models import User
from movies.models import Movie, Genre, Director, Actor
from reviews.models import Review, Comment, Reply


class SimpleUserSerializer(serializers.ModelSerializer):
    """
    간단한 사용자 Serializer: 역참조 시 사용
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'introduction')


class SimpleMovieSerializer(serializers.ModelSerializer):
    """
    간단한 영화 Serializer: 역참조 시 사용
    """
    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_image_url', 'release_date')


class SimpleReviewSerializer(serializers.ModelSerializer):
    """
    간단한 리뷰 Serializer: 역참조 시 사용
    """
    class Meta:
        model = Review
        fields = ('id', 'title', 'rating', 'created_at')
