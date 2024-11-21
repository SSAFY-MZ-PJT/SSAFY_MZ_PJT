# reviews/urls.py

from django.urls import path, include
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.all_review_list, name='all_review_list'), # 전체 리뷰 조회
    path('<int:movie_pk>/', views.movie_review_list_create, name='movie_review_list_create'), # 특정 영화에 대한 리뷰 리스트 조회 (GET) 및 특정 영화에 대한 리뷰 작성 (POST)
    path('<int:review_pk>/', views.review_detail, name='review_detail'), # 리뷰 상세 조회, 리뷰 삭제, 리뷰 수정
    path('<int:review_pk>/comments/', views.comment_list_create, name='comment_list_create'),
    path('<int:review_pk>/comments/<int:comment_pk>/', views.comment_detail, name='comment_detail'),
    path('<int:review_pk>/comments/<comment_pk>/replies/', views.reply_list_create, name='reply_list_create'),
    path('like/<int:review_pk>/', views.review_like, name='review_like'),
    path('like/<int:comment_pk>/', views.comment_like, name='comment_llike'),
]