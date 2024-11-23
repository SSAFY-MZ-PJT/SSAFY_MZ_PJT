# accounts/urls.py

from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    
    # Custom 엔드포인트
    path('<int:user_pk>/', views.user_detail, name='user_detail'), # 회원 정보 조회, 회원 탈퇴, 회원 정보 수정
    # path('<int:user_pk>/password/', views.change_password, name='change_password'), # 기본 url로 가능할지
    path('<int:user_pk>/follow/', views.user_follow, name='user_follow'), # 회원 간 팔로우 | 리스트 조회
    path('<int:user_pk>/like/movies/', views.like_movies, name='like_movies'), # 좋아요한 영화 조회, 영화 좋아요
    path('<int:user_pk>/like/reviews/', views.like_reviews, name='like_reviews'), # 좋아요한 리뷰 조회, 리뷰 좋아요
    path('<int:user_pk>/write/reviews/', views.write_reviews, name='write_reviews'), # 작성한 리뷰 조회
    path('<int:user_pk>/recommended/movies/', views.recommended_movies, name='recommended_movies'), # 추천하는 영화 조회
    
    path('confirm-email/', views.email_confirmation, name='account_confirm_email'),   
    path('csrf/', views.csrf_token, name='csrf_token'),
]
