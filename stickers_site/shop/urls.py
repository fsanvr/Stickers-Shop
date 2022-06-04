import imp
from operator import index
from django.urls import path

from .views import *

urlpatterns = [
    path(route='', view=index, name='index'),
    path(route='register', view=register, name='register'),
    path(route='login/', view=user_login, name='login'),
    path(route='logout/', view=user_logout, name='logout'),
    path(route='profile/', view=profile, name='profile'),
]