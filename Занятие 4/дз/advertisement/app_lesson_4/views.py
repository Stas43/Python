from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("Домашняя")

def lesson(request):
    return HttpResponse("Домашка по 4 занятию")
