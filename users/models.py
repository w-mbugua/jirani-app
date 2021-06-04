from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    neighborhood = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50, null=True, blank=True)
