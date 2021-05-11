from django.contrib import admin
from api.views import *
from api.urls import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),

]
