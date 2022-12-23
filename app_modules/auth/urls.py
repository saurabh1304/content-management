# -*- coding: utf-8 -*-
from app_modules.auth.views import CustomRegistrationViewSet
from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth.views import LoginView, LogoutView
from django.urls import path
from rest_framework.routers import DefaultRouter

app_name = "auth"

router = DefaultRouter()
router.register(r"registration", CustomRegistrationViewSet, basename="user_registration")

urlpatterns = [
    path("login/", LoginView.as_view(), name="user_login"),
    path("token/refresh/", get_refresh_view().as_view(), name="token_refresh"),
    path("logout/", LogoutView.as_view(), name="user_logout"),
] + router.urls
