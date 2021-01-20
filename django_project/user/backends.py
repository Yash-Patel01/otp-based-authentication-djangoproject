from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import User, OneTimePassword


class CustomBackend(BaseBackend):
    def authenticate(self, request, phone_number=None, password=None, otp=None, **kwargs):
        try:
            user = User.objects.get(phone_number=phone_number)
            one_time_password = OneTimePassword.objects.get(user=user)
            otp_valid = (one_time_password.otp == otp)
            if otp_valid:
                return user
        except:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
