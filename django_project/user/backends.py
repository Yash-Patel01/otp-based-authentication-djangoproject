from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password
from .models import User


class CustomBackend(BaseBackend):
    def authenticate(self, request, username=None, otp=None):
        user = User.objects.get(phone_number=username)
        otp_valid = (user.otp == otp)
        if otp_valid:
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
