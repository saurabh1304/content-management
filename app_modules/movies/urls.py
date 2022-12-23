# -*- coding: utf-8 -*-
from rest_framework.routers import DefaultRouter

from app_modules.movies.views import CastViewSet, MoviesViewSet


app_name = "movies"

router = DefaultRouter()

router.register(r"movies", MoviesViewSet, basename="movies")
router.register(r"cast", CastViewSet, basename="cast")

urlpatterns = router.urls
