

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=15, help_text='Required. 15 characters or fewer. Letters, digits and @/./+/-/_ only.')
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username','email','password1','password2' ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model =Profile
        fields = ['image']
