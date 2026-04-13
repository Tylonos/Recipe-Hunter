
from django.shortcuts import render, get_object_or_404
from .models import Recipe, Ingredient
from .models import Recipe
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserRegisterForm, ProfileForm
from .models import Profile


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


def register(request):
    if request.method =='POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            # A Profile is automatically created by the post_save signal for User.
            # Use get_or_create to avoid UNIQUE constraint errors when a Profile
            # already exists for the newly created user.
            profile, created = Profile.objects.get_or_create(user=user)
            # If the form uploaded an image, update the profile image.
            image = profile_form.cleaned_data.get('image')
            if image:
                profile.image = image
                profile.save()
            messages.success(request,'Your account has been created. You can now log in.')
            return redirect('recipes:login')
    else:
        user_form = UserRegisterForm()
        profile_form =ProfileForm()
    return render(request, 'recipes/register.html',{'user_form': user_form, 'profile_form': profile_form})


class CustomLoginView(LoginView):
    template_name ='recipes/login.html'


class CustomLogoutView(LogoutView):
    next_page ='recipes:login'


@login_required
def account(request):
    return render(request, 'recipes/account.html')