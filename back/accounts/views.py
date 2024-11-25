# accounts/views.py

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from accounts.serializers import UserSerializer, UserUpdateSerializer
from movies.serializers import MovieSerializer
from reviews.serializers import ReviewSerializer
from accounts.models import User
from movies.models import Movie

from allauth.account.models import EmailConfirmationHMAC
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import get_user_model

User = get_user_model()


@ensure_csrf_cookie
def csrf_token(request):
    return JsonResponse({'message': 'CSRF cookie set'})

# 이메일 인증 뷰
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])  # 권한 설정
@authentication_classes([])      # 인증 클래스 비움
@ensure_csrf_cookie
def email_confirmation(request):
    
    if request.method == 'GET':
        return Response({'message': 'Ready for email confirmation'})
        
    elif request.method == 'POST':
        try:
            key = request.data.get('key')
            if not key:
                return Response(
                    {'message': 'Invalid key'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )

            email_confirmation = EmailConfirmationHMAC.from_key(key)
            if not email_confirmation:
                return Response(
                    {'message': 'Invalid confirmation link'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            email_confirmation.confirm(request)
            return Response(
                {'message': 'Email successfully confirmed'},
                status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


def get_user_or_403(request, username):
    """
    공통으로 사용하는 사용자 객체 가져오기 함수
    """
    user = get_object_or_404(User, username=username)
    if user != request.user:
        raise PermissionDenied("권한이 없습니다.")
    return user


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user_detail(request):
    """
    현재 로그인한 사용자 정보 반환
    """
    serializer = UserSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def user_detail(request, username):
    user = get_object_or_404(User, username=username)
    is_current_user = request.user == user  # 현재 사용자 여부 확인
    

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response({
            "profile": serializer.data,
            "is_current_user": is_current_user  # 현재 사용자 여부 추가
        }, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        if not is_current_user:  # 권한 확인
            return Response({"error": "You can only delete your own account."}, status=status.HTTP_403_FORBIDDEN)
        
        # 연관된 데이터 안전 삭제
        user.reviews.all().delete()
        user.comments.all().delete()
        user.liked_reviews.clear()
        user.followers.clear()
        user.followings.clear()
        user.delete()
        return Response({"message": "회원 탈퇴가 완료되었습니다."}, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        if not is_current_user:  # 권한 확인
            return Response({"error": "You can only update your own account."}, status=status.HTTP_403_FORBIDDEN)
        serializer = UserUpdateSerializer(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_follow(request, username):
    user_to_follow = get_object_or_404(User, username=username)

    if request.method == 'GET':
        data = {
            "followers": [{"id": f.id, "username": f.username} for f in user_to_follow.followers.all()],
            "followings": [{"id": f.id, "username": f.username} for f in user_to_follow.followings.all()],
        }
        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        if user_to_follow == request.user:
            return Response({"error": "자기 자신을 팔로우할 수 없습니다."}, status=status.HTTP_400_BAD_REQUEST)

        if user_to_follow in request.user.followings.all():
            request.user.followings.remove(user_to_follow)
            return Response({"message": "언팔로우 성공", "is_following": False}, status=status.HTTP_200_OK)
        else:
            request.user.followings.add(user_to_follow)
            return Response({"message": "팔로우 성공", "is_following": True}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def like_movies(request, username):
    user = get_user_or_403(request, username)
    if isinstance(user, Response):
        return user

    liked_movies = user.liked_movies.all()
    serializer = MovieSerializer(liked_movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def like_reviews(request, username):
    user = get_user_or_403(request, username)
    if isinstance(user, Response):
        return user

    liked_reviews = user.liked_reviews.all()
    serializer = ReviewSerializer(liked_reviews, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def write_reviews(request, username):
    user = get_user_or_403(request, username)
    if isinstance(user, Response):
        return user

    reviews = user.reviews.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommended_movies(request, username):
    user = get_user_or_403(request, username)
    if isinstance(user, Response):
        return user

    favorite_genres = user.favorite_genres.all()
    if not favorite_genres:
        return Response({"message": "좋아하는 장르를 설정해주세요."}, status=status.HTTP_400_BAD_REQUEST)

    recommended_movies = Movie.objects.filter(genres__in=favorite_genres).distinct()
    serializer = MovieSerializer(recommended_movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
