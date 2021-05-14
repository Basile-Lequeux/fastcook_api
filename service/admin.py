from django.contrib import admin

from django.contrib import admin

from service.object.user import User
from service.object.recipe import Recipe


admin.site.register(Recipe)
admin.site.register(User)