from django.urls import path
from django.conf.urls.static import static
from watch_and_chat import settings

from .views import *

urlpatterns = [
    path('', index),
    path('film/<slug:name_obj>', film),
    path('serial/<slug:name_obj>', serial),
    path('cartoon/<slug:name_obj>', cartoon),
    path('animated_series/<slug:name_obj>', animated_series),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    