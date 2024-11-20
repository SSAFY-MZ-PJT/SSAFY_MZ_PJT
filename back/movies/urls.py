# movies/urls.py

from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.main_page, name='main_page'), # 메인 페이지 (인기 영화, 현재 상영중인 영화, 영화 관련 뉴스 보여주기)
    # path('guide/', views.guide, name='guide'), # 서비스 소개
    path('now_playing/', views.now_playing_movies, name='now_playing'), # 현재 상영중인 영화 조회
    path('popular/', views.popular_movies, name='popular'), # 인기 영화 조회
    path('all/', views.movie_list, name='movie-list'), # 모든 영화 조회
    # path('news/', views.news, name='news'), # 영화 뉴스 조회 (api 이용)
    path('<int:movie_pk>/', views.movie_detail, name='movie_detail'), # 영화 상세 조회
    path('like/<int:movie_pk>/', views.movie_like, name='movie_like'),  # 영화 좋아요
    path('search/', views.movie_search, name='movie_search'),  # 검색
]