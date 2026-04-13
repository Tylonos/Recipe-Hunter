from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .models import Recipe
from .models import Profile, Ingredient, RecipeIngredient

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]


# Show recipes on the User admin page; do not register Profile as a separate model
try:
	# unregister default UserAdmin then register extended one
	admin.site.unregister(User)
except Exception:
	pass


class CustomUserAdmin(UserAdmin):
	inlines = UserAdmin.inlines + [RecipeInline] if getattr(UserAdmin, 'inlines', None) else [RecipeInline]

admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)
admin.site.register( Profile)
