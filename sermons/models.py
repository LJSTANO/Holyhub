# models.py
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models


class PrayerRequest(models.Model):
    name = models.CharField(max_length=100,default='Prayer for Family')
    email = models.EmailField(default='<EMAIL>',unique=True)
    phone_number = models.CharField(max_length=10,default='07')  # Add phone number field
    request = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prayer Request by {self.name}"


# Sermon Model
class Sermon(models.Model):
    title = models.CharField(max_length=200)
    speaker = models.CharField(max_length=100)
    sermon_date = models.DateField()
    youtube_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


# Daily Devotion Model
class DailyDevotion(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title


