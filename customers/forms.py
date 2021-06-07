from django import forms
from django.contrib.auth.forms import User
from .models import *

PAYMENT_METHOD =[
    (0, 'Thanh toán khi nhận hàng'),
    (1, 'Thanh toán qua thẻ ngân hàng'),
    (2, 'Thanh toán qua ví momo ')
]

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
   
class ReceiverForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput())
    phone = forms.CharField(widget=forms.TextInput())
    house_number = forms.CharField(widget=forms.TextInput())
    commune = forms.CharField(widget=forms.TextInput())
    district = forms.CharField(widget=forms.TextInput())
    city = forms.CharField(widget=forms.TextInput())
    note = forms.CharField(widget=forms.Textarea(), required=False)
    
class PaymentMethodForm(forms.Form):
    method =  forms.ChoiceField(choices = PAYMENT_METHOD)
    
class OrderForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput())
    phone = forms.CharField(widget=forms.TextInput())
    house_number = forms.CharField(widget=forms.TextInput())
    commune = forms.CharField(widget=forms.TextInput())
    district = forms.CharField(widget=forms.TextInput())
    city = forms.CharField(widget=forms.TextInput())
    note = forms.CharField(widget=forms.Textarea())
    total = forms.IntegerField(widget=forms.NumberInput())
    fee_ship = forms.IntegerField(widget=forms.NumberInput())
    into_money = forms.IntegerField(widget=forms.NumberInput())
    method = forms.CharField(widget=forms.TextInput())