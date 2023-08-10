from django.http import HttpResponse
from django.shortcuts import render
from .models import  Advertisement


def index(request):
    adverts = Advertisement.objects.all()
    context = {'adverts': adverts}
    return render(request, 'index.html', context)


def topsellers(request):
    return render(request, 'top-sellers.html')
