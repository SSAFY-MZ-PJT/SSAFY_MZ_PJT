from django.urls import path, include
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.review_list_create),
]