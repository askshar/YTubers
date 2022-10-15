from django.db import models
from datetime import datetime

# Create your models here.

class Hiretuber(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    tuber_id = models.IntegerField()
    tubername = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    message = models.TextField()
    user_id = models.IntegerField(blank=True)
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email
    