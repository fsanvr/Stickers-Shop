from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from operator import index
from .views import *


urlpatterns = [
    path(route='', view=index, name='index'),
    path(route='register', view=register, name='register'),
    path(route='login/', view=user_login, name='login'),
    path(route='logout/', view=user_logout, name='logout'),
    path(route='profile/', view=my_profile, name='my_profile'),
    path(route='profile/<str:username>', view=profile, name='profile'),
    path(route='add_cart/', view=add_cart, name='add_cart'),
    path(route='del_cart/', view=del_cart, name='del_cart'),
    path(route='cart/', view=cart, name='cart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)