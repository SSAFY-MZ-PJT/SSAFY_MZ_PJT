# accounts/serializers.py

from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings
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
    
class CustomAccountAdapter(DefaultAccountAdapter):
    """
    이메일 인증 메시지 및 동작을 커스터마이징하기 위한 어댑터
    """
    def send_mail(self, template_prefix, email, context):
        # 이메일 인증 URL 수정
        context["activate_url"] = f"{settings.FRONTEND_URL}/activate/{context['key']}"
        super().send_mail(template_prefix, email, context)
    

class CustomLoginSerializer(LoginSerializer):
    def validate(self, attrs):
        user = super().validate(attrs)
        if not self.user.is_active:
            raise serializers.ValidationError("이메일 인증이 필요합니다.")
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
    liked_movies = MovieSerializer(many=True, read_only=True, source='liked_movies')
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