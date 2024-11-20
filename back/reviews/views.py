# reviews/views.py

from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import ReviewListSerializer, ReviewSerializer, CommentSerializer
from .models import Review, Comment
from movies.models import Movie


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_review_list(request):
    """
    전체 리뷰 조회
    """
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def movie_review_list_create(request, movie_pk):
    """
    특정 영화에 대한 리뷰 조회 및 작성
    """
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'GET':
        reviews = movie.reviews.all()  # 특정 영화에 연결된 리뷰
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)  # 유저와 영화를 연결하여 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        

@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def review_detail(request, review_pk):
    """
    리뷰 상세 조회, 수정, 삭제
    """
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        if review.user != request.user:
            return Response({"error": "삭제 권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)
        review.delete()
        return Response({"message": "리뷰가 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        if review.user != request.user:
            return Response({"error": "수정 권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)
        serializer = ReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, review_pk):
    """
    댓글 작성
    """
    review = get_object_or_404(Review, pk=review_pk)  # 특정 리뷰 확인

    # 요청 데이터에 user 및 review 정보 추가
    data = request.data.copy()
    data['review'] = review.pk
    data['user'] = request.user.pk

    serializer = CommentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def comment_detail(request, review_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk, review_id=review_pk)

    if request.method == 'DELETE':
        # 작성자 확인
        if comment.user != request.user:
            return Response({"error": "삭제 권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)

        comment.delete()
        return Response({"message": "댓글이 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        # 작성자 확인
        if comment.user != request.user:
            return Response({"error": "수정 권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)

        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def review_like(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'POST':
        review.likes.add(request.user)
        return Response({"message": "좋아요 완료"}, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        review.likes.remove(request.user)
        return Response({"message": "좋아요 취소"}, status=status.HTTP_204_NO_CONTENT)
