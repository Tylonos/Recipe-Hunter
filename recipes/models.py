from django.db import models


from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    cooking_time = models.IntegerField()
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe_ingredients")
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.ingredient.name} for {self.recipe.title}"