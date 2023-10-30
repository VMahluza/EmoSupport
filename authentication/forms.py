from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

tailwind = "shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"

class LoginForm(AuthenticationForm):
    # username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}))
    # password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            new_data = {   
                "class": tailwind
                # "hx-post": ".",
                # "hx-trigger": "keyup changed delay:500ms",
                # "hx-target": "#recipe-container",
                # "hx-swap": "outerHTML"
            }
            self.fields[str(field)].widget.attrs.update(
                new_data
            )

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        required=True, 
        label="Email", 
        widget=forms.EmailInput(attrs={"class": tailwind, "placeholder":"Email"})
        )    
    username = forms.CharField(
        required=True, 
        label="Username", 
        widget=forms.TextInput(attrs={"class":tailwind, "placeholder": "Username"})
    )
    first_name = forms.CharField(
        required=True, 
        label="First Name",  
        widget=forms.TextInput(attrs={"class":tailwind, "placeholder": "First Name"})
    )
    last_name = forms.CharField(
        required=True, 
        label="Last Name",  
        widget=forms.TextInput(attrs={"class":tailwind, "placeholder": "Last Name"})
    )
    password1 = forms.CharField(
        required=True, 
        label="Password",  
        widget=forms.PasswordInput(attrs={"class":tailwind, "placeholder": "Enter your password"})
    )

    password2 = forms.CharField(
        required=True, 
        label="Password",  
        widget=forms.PasswordInput(attrs={"class":tailwind, "placeholder": "Confirm your password"})
    )
    
    # required_css_class = 'form-outline mb-4'
    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'first_name',
            'last_name',
            'gender',
            'password1',
            'password2'
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            new_data = {
                "class": tailwind,
                # "hx-post": ".",
                # "hx-trigger": "keyup changed delay:500ms",
                # "hx-target": "#recipe-container",
                # "hx-swap": "outerHTML"
            }
            self.fields[str(field)].widget.attrs.update(
                new_data
            )
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])   
        user.save()
        if commit:   
            user.save()
        return user