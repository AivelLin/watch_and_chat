from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('film/<slug:name_obj>', film),
    path('serial/<slug:name_obj>', serial),
    path('cartoon/<slug:name_obj>', cartoon),
    path('animated_series/<slug:name_obj>', animated_series),

]