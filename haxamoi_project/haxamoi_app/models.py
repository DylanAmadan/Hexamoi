from django.db import models

from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.CharField(max_length=50)

class Vocabulary(models.Model):
    word = models.CharField(max_length=100)
    meaning = models.TextField()

