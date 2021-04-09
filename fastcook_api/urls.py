from django.contrib import admin
from api.views import *
from api.urls import *
from .views import search_recipes


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('cook', search_recipes)
]
