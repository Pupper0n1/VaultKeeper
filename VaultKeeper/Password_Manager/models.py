from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# Create your models here.

class Password(models.Model):
    website = models.URLField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='passwords')