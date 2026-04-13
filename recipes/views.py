from django.shortcuts import render, get_object_or_404
from .models import Recipe, Ingredient

def recipe_list(request):
    recipes = Recipe.objects.all()
    ingredients = Ingredient.objects.all()
    return render(request, 'recipes/recipe_list.html', {
        'recipes': recipes,
        'ingredients': ingredients
    })

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})