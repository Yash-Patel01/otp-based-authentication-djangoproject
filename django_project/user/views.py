from django.shortcuts import render
from .models import User
from .forms import UserRegisterForm


def home(request):
    return render(request, 'user/home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})
