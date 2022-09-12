from django.shortcuts import render
from django.http import HttpResponse
from .models import Video

# Create your views here.
def index(request):
    films = Video.objects.all()
    context = {'title':'Главная страница для просмотра'}
    return render(request, 'watch/index.html', context)


def video(request):
    return render(request, 'watch/video.html')


def film(request, name_obj):
    return HttpResponse(f"выбор фильма - {name_obj}")


def serial(request, name_obj):
    return HttpResponse(f"выбор сериала - {name_obj}")


def cartoon(request, name_obj):
    return HttpResponse(f"выбор мультфильма - {name_obj}")


def animated_series(request, name_obj):
    return HttpResponse(f"выбор мультсериала - {name_obj}")
    