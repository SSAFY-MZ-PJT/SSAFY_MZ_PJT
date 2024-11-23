# accounts/views.py

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import User
from .serializers import CustomUserDetailsSerializer, MovieSerializer, ReviewSerializer
from movies.models import Movie



@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def user_detail(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)

    if request.method == 'GET':
        # 자신의 정보가 아닌 경우, 팔로우 관련 데이터만 반환하지 않도록 제한 가능
        if user != request.user:
            serializer = CustomUserDetailsSerializer(user)
            return Response(serializer.data, status=200)

        # 자신의 정보는 전체 데이터를 반환
        serializer = CustomUserDetailsSerializer(user)
        return Response(serializer.data, status=200)

    elif request.method == 'DELETE':
        if user != request.user:
            return Response({"error": "권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)
        
        # 사용자와 관련된 데이터 삭제
        user.reviews.all().delete()
        user.comments.all().delete()
        user.liked_reviews.clear()
        user.followers.clear()
        user.followings.clear()
        
        # 사용자 삭제
        user.delete()
        return Response({"message": "회원 탈퇴가 완료되었습니다."}, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        # 요청자가 자신의 계정인지 확인
        if user != request.user:
            return Response({"error": "권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)

        # Serializer를 사용하여 데이터 업데이트
        serializer = CustomUserDetailsSerializer(user, data=request.data, partial=True)  # 부분 수정 허용

        if serializer.is_valid(raise_exception=True):
            serializer.save()  # 부분 수정 적용
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_follow(request, user_pk):
    """
    팔로우 / 팔로잉 목록 조회
    팔로우 / 언팔로우 기능
    """
    if request.method == 'GET':
        user = get_object_or_404(User, pk=user_pk)

        followers = user.followers.all()
        followings = user.followings.all()

        data = {
            "followers": [{"id": follower.id, "username": follower.username} for follower in followers],
            "followings": [{"id": following.id, "username": following.username} for following in followings],
        }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        user_to_follow = get_object_or_404(User, pk=user_pk)

        if user_to_follow == request.user:
            return Response({"error": "자기 자신을 팔로우할 수 없습니다."}, status=status.HTTP_400_BAD_REQUEST)

        # 팔로우 상태 확인
        if user_to_follow in request.user.followings.all():
            # 언팔로우 처리
            request.user.followings.remove(user_to_follow)
            return Response({"message": "언팔로우 성공", "is_following": False}, status=status.HTTP_200_OK)
        else:
            # 팔로우 처리
            request.user.followings.add(user_to_follow)
            return Response({"message": "팔로우 성공", "is_following": True}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def like_movies(request, user_pk):
    """
    좋아요한 영화 조회
    """
    user = get_object_or_404(User, pk=user_pk)
    liked_movies = user.liked_movies.all()  # User 모델에서 역참조
    serializer = MovieSerializer(liked_movies, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def like_reviews(request, user_pk):
    """
    좋아요한 리뷰 조회
    """
    user = get_object_or_404(User, pk=user_pk)
    liked_reviews = user.liked_reviews.all()  # User 모델에서 역참조
    serializer = ReviewSerializer(liked_reviews, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def write_reviews(request, user_pk):
    """
    작성한 리뷰 조회
    """
    user = get_object_or_404(User, pk=user_pk)
    reviews = user.reviews.all()  # User 모델에서 역참조
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommended_movies(request, user_pk):
    """
    회원 맞춤형 추천 영화 조회
    """
    user = request.user

    # 요청된 user_pk와 로그인된 사용자가 동일한지 확인
    if user.pk != user_pk:
        return Response({"error": "권한이 없습니다."}, status=403)

    # 사용자의 좋아하는 장르 가져오기
    favorite_genres = user.favorite_genres.all()

    if not favorite_genres:
        return Response({"message": "좋아하는 장르를 설정해주세요."}, status=400)

    # 좋아하는 장르와 관련된 영화 필터링
    recommended_movies = Movie.objects.filter(genres__in=favorite_genres).distinct()

    # 직렬화 및 응답 반환
    serializer = MovieSerializer(recommended_movies, many=True)
    return Response(serializer.data, status=200)


from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
@ensure_csrf_cookie
def csrf_token(request):
    return JsonResponse({'message': 'CSRF cookie set'})



from allauth.account.models import EmailConfirmationHMAC
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
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