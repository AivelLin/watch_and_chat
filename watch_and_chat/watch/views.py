from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse(f"Главная страница для выбора фильмов")


def film(request, name_obj):
    return HttpResponse(f"выбор фильма - {name_obj}")


def serial(request, name_obj):
    return HttpResponse(f"выбор сериала - {name_obj}")


def cartoon(request, name_obj):
    return HttpResponse(f"выбор мультфильма - {name_obj}")


def animated_series(request, name_obj):
    return HttpResponse(f"выбор мультсериала - {name_obj}")
    