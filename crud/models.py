from django.db import models
from datetime import timedelta, date
import uuid

# Create your models here.


class Song(models.Model):
    Name = models.CharField(max_length=100, null=False, blank=False)
    Duration = models.BigIntegerField(null=False, blank=False)
    Uploaded_time = models.DateTimeField(auto_now=True)


class Podcast(models.Model):
    Name = models.CharField(max_length=100, null=False, blank=False)
    Duration = models.BigIntegerField(null=False, blank=False)
    Uploaded_time = models.DateTimeField(auto_now=True)
    Host = models.CharField(max_length=100, null=False, blank=False)
    Participants = models.TextField(max_length=100, blank=True)


class Audiobook(models.Model):
    Title = models.CharField(max_length=100, null=False, blank=False)
    Author = models.CharField(max_length=100, null=False, blank=False)
    Narrator = models.CharField(max_length=100, null=False, blank=False)
    Duration = models.BigIntegerField(null=False, blank=False)
    Uploaded_time = models.DateTimeField(auto_now=True)
