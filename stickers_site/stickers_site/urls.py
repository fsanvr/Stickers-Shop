from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path(route='admin/', view=admin.site.urls),
    path(route='', view=include('shop.urls')),
]
