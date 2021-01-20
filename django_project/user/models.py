from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=10, unique=True)
    otp = models.CharField(max_length=6, blank=True)
    USERNAME_FIELD = 'phone_number'
