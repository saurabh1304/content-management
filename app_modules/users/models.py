from django.db import models
from app_modules.base.models import BaseModel
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class User(AbstractUser, BaseModel):
    """Default user model"""
    name = models.CharField(_("Name"),max_length=255, blank=True, default="")

    def __str__(self):
        return self.username
