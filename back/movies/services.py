# movies/services.py

from .models import Movie, Director, Actor, Genre
from .utils import fetch_movie_details, fetch_movies_by_genre, fetch_movie_credits, fetch_movies_by_category

def save_movie_by_id(movie_id):
    """
    영화 ID를 사용하여 TMDB에서 데이터를 가져오고 저장합니다.
    """
    # 영화 상세 데이터 가져오기
    movie_data = fetch_movie_details(movie_id)
    save_movie_to_db(movie_data)


def save_movies_by_genre(genre_id, pages=1):
    """
    장르 ID를 사용하여 TMDB에서 데이터를 가져오고 저장합니다.
    """
    for page in range(1, pages + 1):
        movies_data = fetch_movies_by_genre(genre_id, page=page)
        for movie_data in movies_data.get('results', []):
            save_movie_by_id(movie_data['id'])


def save_movie_to_db(movie_data):
    """
    TMDB에서 가져온 영화 데이터를 Django 모델에 저장합니다.
    """
    # 장르 데이터 처리
    genres = []
    for genre_data in movie_data.get('genres', []):
        genre, _ = Genre.objects.get_or_create(name=genre_data['name'])
        genres.append(genre)

    # 감독 데이터 처리
    credits_data = fetch_movie_credits(movie_data['id'])
    director = None
    for crew_member in credits_data.get('crew', []):
        if crew_member['job'] == 'Director':
            director, _ = Director.objects.get_or_create(
                tmdb_id=crew_member['id'],  # TMDB ID 저장
                defaults={
                    'name': crew_member['name'],
                    'photo_url': f"https://image.tmdb.org/t/p/w500{crew_member['profile_path']}" if crew_member.get('profile_path') else None
                }
            )
            break

    # 배우 데이터 처리
    actors = []
    for cast_member in credits_data.get('cast', [])[:10]:  # 최대 10명 저장
        actor, _ = Actor.objects.get_or_create(
            tmdb_id=cast_member['id'],  # TMDB ID 저장
            defaults={
                'name': cast_member['name'],
                'photo_url': f"https://image.tmdb.org/t/p/w500{cast_member['profile_path']}" if cast_member.get('profile_path') else None
            }
        )
        actors.append(actor)

    # 영화 데이터 저장
    movie, created = Movie.objects.get_or_create(
        tmdb_id=movie_data['id'],  # TMDB ID 저장
        defaults={
            'title': movie_data.get('title'),
            'release_date': movie_data.get('release_date'),
            'poster_image_url': f"https://image.tmdb.org/t/p/w500{movie_data.get('poster_path')}" if movie_data.get('poster_path') else None,
            'plot': movie_data.get('overview'),
            'rating': movie_data.get('vote_average'),
            'adult': movie_data.get('adult'),
            'budget': movie_data.get('budget'),
            'revenue': movie_data.get('revenue'),
            'popularity': movie_data.get('popularity'),
            'runtime': movie_data.get('runtime'),
            'tagline': movie_data.get('tagline'),
            'vote_count': movie_data.get('vote_count'),
            'director': director,
        }
    )

    if created:
        movie.genres.set(genres)
        movie.actors.set(actors)

    movie.save()



def save_now_playing_movies(pages=1):
    """
    TMDB API에서 현재 상영 중인 영화를 가져와 데이터베이스에 저장합니다.
    :param pages: 가져올 페이지 수
    """
    movies_data = fetch_movies_by_category('now_playing', pages=pages)
    for movie_data in movies_data:
        save_movie_by_id(movie_data['id'])


def save_popular_movies(pages=1):
    """
    TMDB API에서 인기 영화를 가져와 데이터베이스에 저장합니다.
    :param pages: 가져올 페이지 수
    """
    movies_data = fetch_movies_by_category('popular', pages=pages)
    for movie_data in movies_data:
        save_movie_by_id(movie_data['id'])



def update_movie_categories(pages=1):
    """
    TMDB API를 사용해 현재 상영 중인 영화와 인기 영화 데이터를 업데이트합니다.
    :param pages: 처리할 페이지 수
    """
    # 1. 현재 상영 중인 영화 ID 가져오기
    now_playing_movies = fetch_movies_by_category('now_playing', pages=pages)
    now_playing_ids = {movie['id'] for movie in now_playing_movies}

    # 2. 인기 영화 ID 가져오기
    popular_movies = fetch_movies_by_category('popular', pages=pages)
    popular_ids = {movie['id'] for movie in popular_movies}

    # 3. 데이터베이스에서 영화 상태 업데이트
    movies = Movie.objects.all()
    for movie in movies:
        movie.is_now_playing = movie.tmdb_id in now_playing_ids
        movie.is_popular = movie.tmdb_id in popular_ids
        movie.save()