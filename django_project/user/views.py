from django.shortcuts import render, redirect
from .models import User
from .forms import UserRegisterForm
import random
import math


def generate_otp():
    digits = [i for i in range(0, 10)]
    otp = ""
    for i in range(6):
        index = math.floor(random.random() * 10)
        otp += str(digits[index])
    return otp


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
            return redirect('login')
        else:
            new_otp = generate_otp()
            print(new_otp)
            User.objects.filter(phone_number=phone_number).update(otp=new_otp)
            return redirect('log_in')
    return render(request, 'user/login.html')
