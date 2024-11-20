# reviews/serializers.py

from rest_framework import serializers
from .models import Review, Comment
from movies.models import Movie

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # 댓글 작성자 정보

    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_at', 'updated_at', 'user']


class MovieBriefSerializer(serializers.ModelSerializer):
    """
    리뷰에 연결된 영화 간략한 정보를 포함하는 Serializer
    """
    class Meta:
        model = Movie
        fields = ['id', 'title', 'poster_image_url']


class ReviewListSerializer(serializers.ModelSerializer):
    """
    리뷰 목록에서 간단한 리뷰 정보를 제공하기 위한 Serializer
    """
    class Meta:
        model = Review
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'user']


class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieBriefSerializer(read_only=True)  # 연결된 영화 간략 정보
    comments = CommentSerializer(many=True, read_only=True)  # 연결된 댓글 정보

    class Meta:
        model = Review
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'movie', 'comments']


# 892c41c4380412f20a66d44c9595c0d86f964508