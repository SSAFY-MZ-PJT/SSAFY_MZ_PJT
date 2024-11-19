from django.urls import path
from . import views
from .views import NowPlayingMoviesView, PopularMoviesView

app_name = 'movies'

urlpatterns = [
    # path('', views.main, name='main'),
    # path('guide/', views.guide, name='guide'),
    path('now-playing/', NowPlayingMoviesView.as_view(), name='now-playing'),
    path('popular/', PopularMoviesView.as_view(), name='popular'),
]