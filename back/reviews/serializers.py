# reviews/serializers.py

from rest_framework import serializers
from .models import Review, Comment, Reply
from shared.serializers import SimpleUserSerializer, SimpleMovieSerializer


class ReplySerializer(serializers.ModelSerializer):
    user = SimpleUserSerializer(read_only=True)  # 참조 관계: 작성자 정보

    class Meta:
        model = Reply
        fields = ('id', 'user', 'content', 'created_at', 'updated_at')


class CommentSerializer(serializers.ModelSerializer):
    user = SimpleUserSerializer(read_only=True)
    review = serializers.PrimaryKeyRelatedField(read_only=True)

    # 역참조 관계
    replies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'user', 'review', 'content', 'created_at', 'replies')



class ReviewSerializer(serializers.ModelSerializer):
    user = SimpleUserSerializer(read_only=True)
    movie = SimpleMovieSerializer(read_only=True)

    # 역참조 관계
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    likes = SimpleUserSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = (
            'id', 'user', 'movie', 'title', 'content', 'rating', 'likes', 'comments', 'created_at'
        )
