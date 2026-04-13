from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .models import Recipe, Profile


class RecipeInline(admin.TabularInline):
	model = Recipe
	extra = 0


# Register Recipe normally
admin.site.register(Recipe)


# Show recipes on the User admin page; do not register Profile as a separate model
try:
	# unregister default UserAdmin then register extended one
	admin.site.unregister(User)
except Exception:
	pass


class CustomUserAdmin(UserAdmin):
	inlines = UserAdmin.inlines + [RecipeInline] if getattr(UserAdmin, 'inlines', None) else [RecipeInline]


admin.site.register(User, CustomUserAdmin)
