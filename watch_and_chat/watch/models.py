from django.db import models


# def video_directory_path(instance, filename):
#     return 'uploads/covers/{0}/{1}_cover'.format(instance.video.title, filename)
  

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    cover = models.ImageField(upload_to='uploads/covers/%Y/%m/%d/')
    year = models.CharField(max_length=4)
    length = models.CharField(max_length=15)
    genres = models.CharField(max_length=100)
    rate = models.IntegerField(default=0)
    plot = models.CharField(max_length=800)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)