# movies/management/commands/fetch_update_movie_categories.py

from django.core.management.base import BaseCommand
from movies.services import update_movie_categories

class Command(BaseCommand):
    help = 'Update movie categories (now playing, popular) based on TMDB API'

    def add_arguments(self, parser):
        parser.add_argument('--pages', type=int, default=1, help="Number of pages to fetch for each category")

    def handle(self, *args, **kwargs):
        pages = kwargs['pages']

        # 서비스 레이어 호출
        update_movie_categories(pages=pages)

        self.stdout.write(self.style.SUCCESS(f'Movie categories updated successfully for {pages} pages!'))



# python manage.py update_movie_categories --pages <number_of_pages>


# python dump_data.py