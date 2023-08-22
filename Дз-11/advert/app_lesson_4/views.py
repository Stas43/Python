from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Advertisement
from .forms import MyModelForm


def index(request):
    adverts = Advertisement.objects.all()
    context = {'adverts': adverts}
    return render(request, 'app_adverts/index.html', context)


def topsellers(request):
    return render(request, 'app_adverts/top-sellers.html')

def createAdv(request):
    if request.method == "POST":
        form = MyModelForm(request.POST, request.FILES)
        if form.is_valid():
            advert = Advertisement(**form.cleaned_data)
            advert.user = request.user
            advert.save()
            url = reverse('index')
            return redirect(url)
    else:
        form = MyModelForm()

    context = {'form': form}
    return render(request, 'app_adverts/advertisement-post.html', context)

def reg(request):
    return render(request, 'app_auth/register.html')

def log(request):
    return render(request, 'app_auth/login.html')

def profile(request):
    return render(request, 'app_auth/profile.html')
