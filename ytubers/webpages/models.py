from distutils.command.upload import upload
from django.db import models


class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    fb_link = models.CharField(max_length=255)
    insta_link = models.CharField(max_length=255)
    yt_link = models.CharField(max_length=255, blank=True, null=True)
    photo = models.ImageField(upload_to='media/team/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name    


class Slider(models.Model):
    headline = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    button_text = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='media/slider/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline
    