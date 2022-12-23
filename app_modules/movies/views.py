from app_modules.base.viewsets import BaseModelViewSet
from app_modules.movies.models import Cast, Movie
from app_modules.movies.serializers import CastDetailSerializer, MovieDetailSerializer, MovieSerializer
from rest_framework.exceptions import NotFound

# Create your views here.


class MoviesViewSet(BaseModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        actions = {"retrieve": MovieDetailSerializer}

        if self.action in actions:
            self.serializer_class = actions.get(self.action)
        return super().get_serializer_class()

    def retrieve(self, request, pk=None):
        try:
            Movie.objects.get(id=pk)
        except Movie.DoesNotExist:
            raise NotFound("Movie doesn't exist.")
        return super().retrieve(request, pk)

    def update(self, request, pk=None):
        try:
            Movie.objects.get(id=pk)
        except Movie.DoesNotExist:
            raise NotFound("Movie doesn't exist.")
        return super().retrieve(request, pk)

    def destroy(self, request, pk=None):
        try:
            Movie.objects.get(id=pk)
        except Movie.DoesNotExist:
            raise NotFound("Movie doesn't exist.")
        return super().retrieve(request, pk)


class CastViewSet(BaseModelViewSet):
    serializer_class = CastDetailSerializer
    queryset = Cast.objects.all()

    def get_queryset(self):
        movie = self.request.GET.get("movie")
        if movie:
            return Cast.objects.filter(movie=movie)
        return Cast.objects.all()

    def retrieve(self, request, pk=None):
        try:
            Cast.objects.get(id=pk)
        except Cast.DoesNotExist:
            raise NotFound("Cast doesn't exist.")
        return super().retrieve(request, pk)

    def update(self, request, pk=None):
        try:
            Cast.objects.get(id=pk)
        except Cast.DoesNotExist:
            raise NotFound("Cast doesn't exist.")
        return super().retrieve(request, pk)

    def destroy(self, request, pk=None):
        try:
            Cast.objects.get(id=pk)
        except Cast.DoesNotExist:
            raise NotFound("Cast doesn't exist.")
        return super().retrieve(request, pk)
