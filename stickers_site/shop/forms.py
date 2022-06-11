from dataclasses import fields
import numbers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label='username',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label='password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='repeat password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('username',  'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='username',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )


class CreateStickerForm(forms.ModelForm):
    name = forms.CharField(
        label='name',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    price = forms.IntegerField(
        label='price',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    image = forms.ImageField(
        label='image',
        widget=forms.FileInput(attrs={'class': 'form-control'}),
        
    )
    size = forms.CharField(
        label='size',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    number = forms.IntegerField(
        label='number',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Stickers
        fields = ('name', 'price', 'image', 'size', 'number')
