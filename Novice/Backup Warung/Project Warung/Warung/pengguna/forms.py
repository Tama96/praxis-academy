from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

class penggunaForm(ModelForm):
    class Meta:
        model = models.Pengguna
        exclude = []


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
   
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', )
