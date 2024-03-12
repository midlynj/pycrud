from enum import Enum

from django.db import models
from django_enumfield import enum


# Create your models here.

class Status(enum.Enum):
    ACTIVE = 1
    INACTIVE = 2
    PENDING = 3


class User(models.Model):
    first_name = models.CharField(max_length=100)
    status = models.IntegerField(choices=[(status.value, status.name) for status in Status])

    def __str__(self):
        return self.first_name

    @property
    def status_display(self):
        return Status(self.status).name


class UserDto(models.Model):

    first_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name
