from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Advertisement
from .forms import MyModelForm


def index(request):
    adverts = Advertisement.objects.all()
    context = {'adverts': adverts}
    return render(request, 'index.html', context)


def topsellers(request):
    return render(request, 'top-sellers.html')

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
    return render(request, 'advertisement-post.html', context)

def reg(request):
    return render(request, 'register.html')

def log(request):
    return render(request, 'login.html')
