# reviews/serializers.py

from rest_framework import serializers
from .models import Review, Comment, Reply
from movies.models import Movie

class ReplySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Reply
        fields = ['id', 'content', 'created_at', 'updated_at', 'user']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    replies = serializers.SerializerMethodField()  # 대댓글 목록

    class Meta:
        model = Comment
        fields = ['id', 'content', 'likes', 'created_at', 'updated_at', 'user', 'replies']

    def get_replies(self, obj):
        replies = obj.replies.all()  # 대댓글 가져오기
        return ReplySerializer(replies, many=True).data


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
    likes_count = serializers.SerializerMethodField()  # 좋아요 수를 계산하는 필드

    class Meta:
        model = Review
        fields = ['id', 'title', 'content','rating','created_at', 'updated_at', 'user', 'likes_count']

    def get_likes_count(self, obj):
        return obj.likes.count()  # 좋아요 수 반환


class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieBriefSerializer(read_only=True)  # 연결된 영화 간략 정보
    comments = CommentSerializer(many=True, read_only=True)  # 댓글 및 대댓글 정보 포함
    user = serializers.StringRelatedField(read_only=True)  # user를 읽기 전용으로 설정
    likes_count = serializers.SerializerMethodField()  # 좋아요 수 추가

    class Meta:
        model = Review
        fields = [
            'id',
            'title',
            'content',
            'rating',
            'created_at',
            'updated_at',
            'movie',
            'comments',
            'user',
            'likes_count',
        ]
    