# accounts/urls.py

from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('me/', views.current_user_detail, name='current_user_detail'), # 현재 로그인한 사용자 정보
    path('<str:username>/', views.user_detail, name='user_detail'),  # 회원 정보 조회, 회원 탈퇴, 회원 정보 수정
    path('<str:username>/follow/', views.user_follow, name='user_follow'),  # 회원 간 팔로우 | 리스트 조회
    path('<str:username>/like/movies/', views.like_movies, name='like_movies'),  # 좋아요한 영화 조회
    path('<str:username>/like/reviews/', views.like_reviews, name='like_reviews'),  # 좋아요한 리뷰 조회
    path('<str:username>/write/reviews/', views.write_reviews, name='write_reviews'),  # 작성한 리뷰 조회
    path('<str:username>/recommended/movies/', views.recommended_movies, name='recommended_movies'),  # 추천하는 영화 조회
]
