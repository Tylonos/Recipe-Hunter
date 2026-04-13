from django.contrib import admin

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1
from .models import Recipe
from .models import Profile

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]

admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register( Profile)
