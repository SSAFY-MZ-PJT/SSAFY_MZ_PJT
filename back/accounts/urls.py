# accounts/urls.py

from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    # 기본 Auth 엔드포인트
    path('', include('dj_rest_auth.urls')),  # 로그인/로그아웃
    path('signup/', include('dj_rest_auth.registration.urls')),  # 회원가입
    
    # Custom 엔드포인트
    # path('profile/<int:pk>/', views.UserProfileView.as_view(), name='user-profile'),  # 프로필 조회/수정
]
