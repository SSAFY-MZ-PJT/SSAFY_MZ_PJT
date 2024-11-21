# movies/management/commands/fetch_movies.py

from django.core.management.base import BaseCommand
from movies.services import save_movies_by_genre

class Command(BaseCommand):
    help = 'Fetch movies by genre from TMDB API and save to the database'

    def add_arguments(self, parser):
        parser.add_argument('genre_id', type=int, help="Genre ID to fetch movies for")
        parser.add_argument('--pages', type=int, default=1, help="Number of pages to fetch")

    def handle(self, *args, **kwargs):
        genre_id = kwargs['genre_id']
        pages = kwargs['pages']

        # 서비스 레이어 호출
        save_movies_by_genre(genre_id, pages)

        self.stdout.write(self.style.SUCCESS(f'Fetched and saved {pages} pages of genre {genre_id} movies!'))



# [
#     { "id": 28, "name": "Action" },
#     { "id": 12, "name": "Adventure" },
#     { "id": 16, "name": "Animation" },
#     { "id": 35, "name": "Comedy" },
#     { "id": 80, "name": "Crime" },
#     { "id": 99, "name": "Documentary" },
#     { "id": 18, "name": "Drama" },
#     { "id": 10751, "name": "Family" },
#     { "id": 14, "name": "Fantasy" },
#     { "id": 36, "name": "History" },
#     { "id": 27, "name": "Horror" },
#     { "id": 10402, "name": "Music" },
#     { "id": 9648, "name": "Mystery" },
#     { "id": 10749, "name": "Romance" },
#     { "id": 878, "name": "Science Fiction" },
#     { "id": 10770, "name": "TV Movie" },
#     { "id": 53, "name": "Thriller" },
#     { "id": 10752, "name": "War" },
#     { "id": 37, "name": "Western" }
# ]

# python manage.py fetch_movies <genre_id> --pages <number_of_pages>
# python manage.py fetch_movies 28 --pages 1
# python manage.py fetch_movies 12 --pages 1
# python manage.py fetch_movies 16 --pages 1
# python manage.py fetch_movies 35 --pages 1
# python manage.py fetch_movies 80 --pages 1
# python manage.py fetch_movies 99 --pages 1
# python manage.py fetch_movies 18 --pages 1
# python manage.py fetch_movies 10751 --pages 1
# python manage.py fetch_movies 14 --pages 1
# python manage.py fetch_movies 36 --pages 1
# python manage.py fetch_movies 27 --pages 1
# python manage.py fetch_movies 10402 --pages 1
# python manage.py fetch_movies 9648 --pages 1
# python manage.py fetch_movies 10749 --pages 1
# python manage.py fetch_movies 878 --pages 1
# python manage.py fetch_movies 10770 --pages 1
# python manage.py fetch_movies 53 --pages 1
# python manage.py fetch_movies 10752 --pages 1
# python manage.py fetch_movies 37 --pages 1