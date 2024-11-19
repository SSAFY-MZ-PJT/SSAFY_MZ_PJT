from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer

class NowPlayingMoviesView(APIView):
    def get(self, request):
        movies = Movie.objects.filter(is_now_playing=True)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

class PopularMoviesView(APIView):
    def get(self, request):
        movies = Movie.objects.filter(is_popular=True)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

class MovieListView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)