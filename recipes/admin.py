from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient, Profile


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]


admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)
admin.site.register(Profile)
