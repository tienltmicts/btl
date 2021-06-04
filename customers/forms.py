from django import forms
from django.contrib.auth.forms import User
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(), max_length=255)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=255)
    
    
class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    password_repeat = forms.CharField(widget=forms.PasswordInput())
    name = forms.CharField(widget=forms.TextInput())
    email = forms.EmailField(widget=forms.EmailInput())
    phone = forms.CharField(widget=forms.NumberInput())
   