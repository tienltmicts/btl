from django import forms
from django.contrib.auth.forms import User
from .models import *

class FilterForm(forms.Form):
    item = forms.CharField(widget=forms.TextInput())
    param = forms.CharField(widget=forms.TextInput())
    times = forms.CharField(widget=forms.TextInput())