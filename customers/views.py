from .models import Customer, USER_PROFILE_GENDER_CHOICES
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
import datetime

# Create your views here.
def user_login(request):
    messages = ''
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                request.session.set_expiry(0)
                login(request, user)  
                for group in user.groups.all():
                    if group == "NhanvienNhapkho" or group == "Admin" or group == "nhanvienKinhdoanh":
                        return HttpResponseRedirect('/admin')
                return HttpResponseRedirect('/home')
            else:
                messages = "Tên tài khoản hoặc mật khẩu của bạn không đúng"
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form, 'messages': messages})

def register(request):
    template = 'register.html'
   
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password'],
                )
                user.phone_number = form.cleaned_data['phone']
                user.save()
               
                cus = Customer.objects.create(
                    uid=user,
                    name=form.cleaned_data['name'],
                    email=form.cleaned_data['email'],
                    birthday= datetime.datetime.now(),
                    phone=form.cleaned_data['phone'],
                    
                )
                cus.save()
                
                login(request, user)
               
                # redirect to accounts page:
                return HttpResponseRedirect('/home')

   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()
   
    return render(request, template, {'form': form})


def home(request):
    return render(request, "home.html")
