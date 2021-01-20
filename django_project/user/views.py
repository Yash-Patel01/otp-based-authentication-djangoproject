from django.shortcuts import render, redirect
from .models import User, LoginAttempts
from .forms import UserRegisterForm
import random
import math
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib import messages
from django.utils import timezone
import datetime


def generate_otp():
    digits = [i for i in range(0, 10)]
    otp = ""
    for i in range(6):
        index = math.floor(random.random() * 10)
        otp += str(digits[index])
    return otp


def attempts_left(request, login_attempts):
    if login_attempts.attempts_count < 2 and login_attempts.can_login_after < timezone.now():
        login_attempts.attempts_count += 1
        login_attempts.can_login_after = timezone.now()
        login_attempts.save()
        messages.error(
            request, f'{3-login_attempts.attempts_count}attempts left.')
        return True
    else:
        login_attempts.attempts_count = 0
        login_attempts.can_login_after = timezone.now() + datetime.timedelta(minutes=5)
        login_attempts.save()
        messages.error(
            request, 'Too many failed login attempts. Please try again after some time.')
        return False


def home_view(request):
    return render(request, 'user/home.html')


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print('Welcome to Django Project')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})


def generate_otp_view(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            messages.error(request, 'User does not exist.')
            return redirect('login')
        else:
            new_otp = generate_otp()
            print(new_otp)
            User.objects.filter(phone_number=phone_number).update(otp=new_otp)
            messages.success(request, 'OTP sent successfully.')
            return redirect(f'/log_in/?phone_number={phone_number}')
    return render(request, 'user/login.html')


def login_view(request, **kwargs):
    phone_number = request.GET.get('phone_number', None)
    is_attempts_left = True
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        otp = request.POST.get('otp')
        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            messages.error(request, 'User does not exist.')
            return redirect('login')
        else:
            user_auth = authenticate(phone_number=phone_number, otp=otp)
            try:
                login(request, user_auth)
            except:
                messages.error(request, 'Invalid OTP')
                login_attempts = LoginAttempts.objects.get(user=user)
                is_attempts_left = attempts_left(request, login_attempts)
            else:
                login_attempts = LoginAttempts.objects.get(user=user)
                login_attempts.attempts_count = 0
                login_attempts.can_login_after = timezone.now()
                login_attempts.save()
                return redirect('/')
    return render(request, 'user/log_in.html', {'phone_number': phone_number, 'is_attempts_left': is_attempts_left})
