from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegistrationForm

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Перенаправление на главную страницу, заменить 'home' на вашу URL-страницу
    else:
        form = RegistrationForm()
    return render(request, 'app_auth/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Перенаправление на главную страницу, заменить 'home' на вашу URL-страницу
    else:
        form = LoginForm()
    return render(request, 'app_auth/login.html', {'form': form})


def profile_view(request):
    return render(request, 'app_auth/profile.html')

def logout_view(request):
    logout(request)
    return redirect('index')
