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


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def review_list_create(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializers = ReviewListSerializer(reviews, many=True)
        return Response(serializers.data)
    
    elif request.method == 'POST':
        movie_id = request.data.get('movie_id')  # 영화 ID를 요청 데이터에서 가져옴
        if not movie_id:
            return Response({"error": "영화 ID가 필요합니다."}, status=status.HTTP_400_BAD_REQUEST)
        
        movie = Movie.objects.filter(id=movie_id).first()
        if not movie:
            return Response({"error": "영화를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie) # movie=movie
            return Response(serializer.data)
        

@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
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
