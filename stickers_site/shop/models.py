from distutils.command.upload import upload
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#class Profile(models.Model):
#    username = models.CharField(max_length=30, unique=True)
#    email = models.EmailField(max_length=30, unique=True)
#    password = models.CharField(max_length=500)
#    data = models.DateField(auto_now_add=True)
#
#    def __str__(self):
#        return self.username


class Stickers(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    image = models.ImageField()
    size = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)