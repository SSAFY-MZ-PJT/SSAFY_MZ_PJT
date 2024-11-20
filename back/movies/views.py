# movies/views.py

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Movie
from .serializers import MovieSerializer
from django.db.models import Q
# from rest_framework.pagination import PageNumberPagination


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def main_page(request):
    """
    메인 페이지 데이터 (현재 상영 중인 영화, 인기 영화, 추천 영화)
    """
    user = request.user

    # 현재 상영 중인 영화 (최대 12개)
    now_playing_movies = Movie.objects.filter(is_now_playing=True)[:12]
    now_playing_serializer = MovieSerializer(now_playing_movies, many=True)

    # 인기 영화 (최대 12개)
    popular_movies = Movie.objects.filter(is_popular=True)[:12]
    popular_serializer = MovieSerializer(popular_movies, many=True)

    # 회원 맞춤형 추천 영화 (최대 12개)
    favorite_genres = user.favorite_genres.all()
    if favorite_genres:
        recommended_movies = Movie.objects.filter(genres__in=favorite_genres).distinct()[:12]
        recommended_serializer = MovieSerializer(recommended_movies, many=True)
    else:
        recommended_serializer = []  # 좋아하는 장르가 없을 경우 빈 리스트

    # JSON 데이터 응답
    return Response({
        "now_playing": now_playing_serializer.data,
        "popular": popular_serializer.data,
        "recommended": recommended_serializer if isinstance(recommended_serializer, list) else recommended_serializer.data
    }, status=200)


@api_view(['GET'])
def now_playing_movies(request):
    movies = Movie.objects.filter(is_now_playing=True)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def popular_movies(request):
    movies = Movie.objects.filter(is_popular=True)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_search(request):
    """
    영화 검색 (제목, 장르, 감독, 배우) 및 비슷한 장르의 영화 포함
    """
    query = request.GET.get('query', '').strip()
    if not query:
        return Response({"error": "검색어를 입력해주세요."}, status=400)

    # 1. 검색된 영화
    searched_movies = Movie.objects.filter(
        Q(title__icontains=query) |
        Q(genres__name__icontains=query) |
        Q(director__name__icontains=query) |
        Q(actors__name__icontains=query)
    ).distinct()

    # 2. 비슷한 장르의 영화
    similar_movies = Movie.objects.none()
    if searched_movies.exists():
        related_genres = searched_movies.values_list('genres', flat=True).distinct()
        similar_movies = Movie.objects.filter(genres__in=related_genres).exclude(id__in=searched_movies).distinct()

    # 3. 직렬화 및 응답
    searched_serializer = MovieSerializer(searched_movies, many=True)
    similar_serializer = MovieSerializer(similar_movies, many=True)

    return Response({
        "searched_movies": searched_serializer.data,
        "similar_movies": similar_serializer.data
    }, status=200)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def movie_like(request, movie_pk):
    """
    영화 좋아요 및 좋아요 취소
    """
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'POST':
        # 좋아요 추가
        movie.likes.add(request.user)
        return Response({"message": "영화 좋아요 완료"}, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        # 좋아요 취소
        movie.likes.remove(request.user)
        return Response({"message": "영화 좋아요 취소 완료"}, status=status.HTTP_204_NO_CONTENT)