from django.contrib.auth.forms import UserCreationForm#, UserChangeForm
from users.models import User
from django import forms
from products.forms import StyleFormMixin


class UserRegisterForm(UserCreationForm, StyleFormMixin):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

