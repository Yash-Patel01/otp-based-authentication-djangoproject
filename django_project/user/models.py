from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    phone_number = models.CharField(max_length=10, unique=True)
    USERNAME_FIELD = 'phone_number'


class OneTimePassword(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6, blank=True)
    created_at = models.DateTimeField(default=timezone.now)


class LoginAttempts(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    attempts_count = models.IntegerField(default=0)
    can_login_after = models.DateTimeField(default=timezone.now)


class Emails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.FileField()
    primary = models.BooleanField()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_login_attempts(sender, instance=None, created=False, **kwargs):
    if created:
        LoginAttempts.objects.create(user=instance)
        OneTimePassword.objects.create(user=instance)
