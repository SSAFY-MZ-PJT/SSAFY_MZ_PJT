# accounts/serializers.py

from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User
from movies.models import Movie, Genre
from reviews.models import Review


class CustomRegisterSerializer(RegisterSerializer):
    email = serializers.EmailField(required=True)  # 이메일 필수
    favorite_genres = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(), many=True, required=False  # 좋아하는 장르 필수
    )

    def save(self, request):
        user = super().save(request)
        user.email = self.validated_data.get('email', '')
        favorite_genres = self.validated_data.get('favorite_genres', [])
        user.favorite_genres.set(favorite_genres)  # 좋아하는 장르 설정
        user.save()
        return user


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'poster_image_url', 'release_date', 'plot']


class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'movie')


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    favorite_genres = serializers.StringRelatedField(many=True, read_only=True)
    followers = serializers.StringRelatedField(many=True, read_only=True)
    followings = serializers.StringRelatedField(many=True, read_only=True)
    liked_movies = MovieSerializer(many=True, read_only=True, source='like_movies')
    liked_reviews = ReviewSerializer(many=True, read_only=True, source='liked_reviews')
    written_reviews = ReviewSerializer(many=True, read_only=True, source='reviews')

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'profile_image',
            'favorite_genres',
            'followers',
            'followings',
            'liked_movies',
            'liked_reviews',
            'written_reviews',
        )