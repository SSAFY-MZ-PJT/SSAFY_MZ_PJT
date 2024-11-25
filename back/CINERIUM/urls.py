"""
URL configuration for CINERIUM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import email_confirmation, csrf_token

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # 회원가입, 로그인, 로그아웃, 비밀번호 변경
    path('accounts/', include('dj_rest_auth.urls')),  # 로그인, 로그아웃
    path('accounts/signup/', include('dj_rest_auth.registration.urls')), # 회원가입

    # 회원 프로필 관련
    path('accounts/', include('accounts.urls')),

    # 영화, 리뷰, 토론
    path('movies/', include('movies.urls')),
    path('reviews/', include('reviews.urls')),
    path('chats/', include('chats.urls')),

    
    # 이메일 인증
    path('accounts', include('allauth.urls')), # 이메일 인증
    path('confirm-email/', email_confirmation, name='account_confirm_email'),
    path('csrf/', csrf_token, name='csrf_token'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
