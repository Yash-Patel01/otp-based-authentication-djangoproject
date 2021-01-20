from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ['phone_number', 'username', 'first_name', 'last_name', 'email',
                  'password1', 'password2']
