# movies/utils.py

import requests
from django.conf import settings

API_KEY = settings.TMDB_API_KEY
BASE_URL = 'https://api.themoviedb.org/3'
DEFAULT_LANGUAGE = 'en-US'  # 기본 언어를 한국어로 설정

def fetch_movie_details(movie_id):
    """
    특정 영화의 상세 정보를 TMDB API에서 가져옵니다.
    """
    url = f"{BASE_URL}/movie/{movie_id}"
    response = requests.get(url, params={"api_key": API_KEY, "language": DEFAULT_LANGUAGE})
    response.raise_for_status()
    return response.json()


def fetch_movies_by_genre(genre_id, page=1):
    """
    특정 장르의 영화를 가져옵니다.
    """
    url = f"{BASE_URL}/discover/movie"
    response = requests.get(url, params={
        "api_key": API_KEY,
        "language": DEFAULT_LANGUAGE,
        "sort_by": "popularity.desc",
        "with_genres": genre_id,
        "page": page
    })
    response.raise_for_status()
    return response.json()


def fetch_movie_credits(movie_id):
    """
    특정 영화의 크레딧 정보를 가져옵니다 (감독, 배우 등).
    """
    url = f"{BASE_URL}/movie/{movie_id}/credits"
    response = requests.get(url, params={"api_key": API_KEY, "language": DEFAULT_LANGUAGE})
    response.raise_for_status()
    return response.json()


def fetch_movies_by_category(category, pages=1):
    """
    특정 카테고리 (popular, now_playing 등)의 여러 페이지의 영화를 가져옵니다.
    :param category: 카테고리 이름 (예: 'popular', 'now_playing')
    :param pages: 가져올 페이지 수
    :return: 모든 페이지에서 가져온 영화 리스트
    """
    all_movies = []
    for page in range(1, pages + 1):
        url = f"{BASE_URL}/movie/{category}"
        response = requests.get(url, params={"api_key": API_KEY, "language": DEFAULT_LANGUAGE, "page": page})
        response.raise_for_status()
        data = response.json()
        all_movies.extend(data.get('results', []))  # 각 페이지의 결과를 누적
    return all_movies

