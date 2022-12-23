from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter


router = DefaultRouter()

app_name = "api"

urlpatterns = [
    path("rest-auth/", include("app_modules.auth.urls")),
    path("", include("app_modules.users.urls")),
    path("", include("app_modules.movies.urls")),
]
