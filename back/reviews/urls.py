# reviews/urls.py

from django.urls import path, include
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.review_list_create, name='review_list_create'),
    path('<int:review_pk>/', views.review_detail, name='review_detail'),
    path('<review_pk>/comments/', views.comment_create, name='comment_create'),
    path('<review_pk>/comments/<comment_pk>/', views.comment_detail, name='comment_detail'),
    path('like/<int:review_pk>/', views.review_like, name='review_like'),
]