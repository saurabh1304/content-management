# -*- coding: utf-8 -*-
from rest_framework.routers import DefaultRouter

from app_modules.users.views import UserProfileViewSet


app_name = "users"

router = DefaultRouter()

router.register(r"user", UserProfileViewSet, basename="user")

urlpatterns = router.urls
