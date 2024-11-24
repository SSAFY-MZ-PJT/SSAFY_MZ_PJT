# accounts/serializers.py

from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from movies.models import Genre
from shared.serializers import SimpleMovieSerializer, SimpleReviewSerializer
from movies.serializers import GenreSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
    username = serializers.CharField(required=True)  # 필수
    email = serializers.EmailField(required=True)    # 필수
    favorite_genres = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(), many=True, required=True
    )  # 필수
    introduce = serializers.CharField(required=False, allow_blank=True)  # 선택

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'favorite_genres', 'introduce']

    def validate_favorite_genres(self, value):
        if not value:
            raise serializers.ValidationError("You must select at least one favorite genre.")
        return value

    def save(self, request):
        user = super().save(request)
        user.username = self.validated_data.get('username')
        user.email = self.validated_data.get('email')
        user.introduce = self.validated_data.get('introduce', "")
        user.save()
        user.favorite_genres.set(self.validated_data.get('favorite_genres'))  # ManyToMany 저장
        return user


class CustomLoginSerializer(LoginSerializer):
    username = None  # username 필드 제거
    email = serializers.EmailField(required=True)  # email 필수

    def validate_email(self, value):
        """
        이메일 존재 여부 확인
        """
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("No account found with this email.")
        return value
    

class UserUpdateSerializer(serializers.ModelSerializer):
    """
    회원정보 수정 Serializer
    - 수정 가능 필드: profile_image, introduce, favorite_genres
    """
    profile_image = serializers.ImageField(required=False)
    introduce = serializers.CharField(required=False, allow_blank=True)
    favorite_genres = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(), many=True, required=False
    )

    class Meta:
        model = User
        fields = ['profile_image', 'introduce', 'favorite_genres']

    def update(self, instance, validated_data):
        """
        사용자 정보 업데이트 로직
        """
        # 프로필 이미지 업데이트
        if 'profile_image' in validated_data:
            instance.profile_image = validated_data['profile_image']

        # 소개글 업데이트
        if 'introduce' in validated_data:
            instance.introduce = validated_data['introduce']

        # 선호 장르 업데이트
        if 'favorite_genres' in validated_data:
            instance.favorite_genres.set(validated_data['favorite_genres'])

        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    followers = serializers.StringRelatedField(many=True, read_only=True)
    followings = serializers.StringRelatedField(many=True, read_only=True)
    favorite_genres = GenreSerializer(many=True, read_only=True)

    # 역참조 관계
    liked_movies = SimpleMovieSerializer(many=True, read_only=True)
    liked_reviews = SimpleReviewSerializer(many=True, read_only=True)
    reviews = SimpleReviewSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'profile_image', 'followers', 'followings',
            'favorite_genres', 'liked_movies', 'liked_reviews', 'reviews'
        )
