# movies/management/commands/fetch_popular_movies.py

from django.core.management.base import BaseCommand
from movies.services import save_popular_movies

class Command(BaseCommand):
    help = 'Fetch popular movies from TMDB API and save to the database'

    def add_arguments(self, parser):
        parser.add_argument('--pages', type=int, default=1, help="Number of pages to fetch")

    def handle(self, *args, **kwargs):
        pages = kwargs['pages']

        # 서비스 레이어 호출
        save_popular_movies(pages)

        self.stdout.write(self.style.SUCCESS(f'Fetched and saved popular movies for {pages} pages!'))


# python manage.py fetch_popular_movies --pages <number_of_pages>