from django.contrib import admin

from django.contrib import admin
from service.models.ingredient import Ingredient
from service.models.user import User
from service.models.recipe import Recipe


admin.site.register(Recipe)
admin.site.register(User)