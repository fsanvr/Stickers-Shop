import imp
from operator import index
from django.urls import path

from .views import *

urlpatterns = [
    path(route='', view=index),
]