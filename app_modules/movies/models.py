from enum import IntEnum

from app_modules.base.models import BaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Movie(BaseModel):
    """
    Movie
    """

    title = models.CharField(_("Title"), max_length=255)
    runtime = models.PositiveIntegerField(_("Run Time"))
    language = models.CharField(_("Tag Line"), max_length=50)
    tagline = models.CharField(_("Tag Line"), max_length=255)


class Gender(IntEnum):

    MALE = 1
    FEMALE = 2
    TRANS = 3
    NON_BINARY = 4

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class Cast(BaseModel):
    """
    Movie Cast
    """

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.CharField(_("Name"), max_length=50)
    gender = models.IntegerField(_("Gender"), choices=Gender.choices(), default=Gender.MALE)
    dob = models.DateField(_("DOB"))
    