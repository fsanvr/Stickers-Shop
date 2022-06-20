from django.contrib.auth.models import User
from django.db import models


class Stickers(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images')
    size = models.CharField(max_length=30, blank=True, default='')
    number = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)