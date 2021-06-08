from django.contrib import admin
from api import viewsets
from api.urls import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
]
