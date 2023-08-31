from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Advertisement
from .forms import MyModelForm
from django.contrib.auth import get_user_model
from django.db.models import Count

User = get_user_model()


def index(request):
    titel = request.GET.get('query')
    if titel:
        adverts = Advertisement.objects.filter(titel__icontains=titel)
    else:
        adverts = Advertisement.objects.all()
    context = {'adverts': adverts, 'query': titel }
    return render(request, 'app_adverts/index.html', context)


def topsellers(request):
    users = User.objects.annotate(adv_count=Count('advertisement')).order_by('-adv_count')
    context = {'users': users}
    return render(request, 'app_adverts/top-sellers.html', context)

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


def advDetails(request, pk):
    advert = Advertisement.objects.get(id=pk)
    context = {
        'advert': advert
    }

    return render(request, 'app_adverts/advertisement.html', context)