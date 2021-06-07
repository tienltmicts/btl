from typing import cast
from warehouse.models import Book, Clothes, Electro
from produces.models import *
from .models import *
from django.shortcuts import render,get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from .forms import LoginForm, OrderForm, PaymentMethodForm, ReceiverForm, RegisterForm
from django.contrib.auth.models import User
import datetime
from django.views.decorators.csrf import csrf_protect


# Create your views here.
@csrf_protect
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
                    print(group)
                    if group.name == "NhanvienNhapkho" or group.name == "Admin" or group.name == "NhanvienKinhdoanh":
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
                
                cart = Cart.objects.create(
                    customer = cus
                )
                cart.save()
                
                login(request, user)
               
                # redirect to accounts page:
                return HttpResponseRedirect('/home')

   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()
   
    return render(request, template, {'form': form})


def home(request):
    cus= get_object_or_404(Customer, uid=request.user)
    cart= get_object_or_404(Cart, customer=cus)
    cart_clothes = CartClothes.objects.filter(cart=cart)
    cart_electro = CartElectro.objects.filter(cart=cart)
    cart_book = CartBook.objects.filter(cart=cart)
    amount = len(cart_clothes) + len(cart_book) + len(cart_electro)
    clothes = []
    electros =[]
    books = []
    total = 0
    for i in ItemClothes.objects.all():
        clothes.append(i)
        
    for i in ItemElectro.objects.all():
        electros.append(i)
    
    for i in ItemBook.objects.all():
        books.append(i)

    
    return render(request, "home.html", {
        'clothes': clothes,
        'electros': electros,
        'books': books,
        'amount': amount
    })

def add_cart_clothes(request, id):
    cus = get_object_or_404(Customer, uid=request.user)
    cart = get_object_or_404(Cart, customer=cus)
    clothes = get_object_or_404(ItemClothes,id=id)
    price = clothes.price
    sale_off = clothes.sale_off
    real_pay = price
    if sale_off != 0:
        real_pay = (price * sale_off)/100
    
    if CartClothes.objects.filter(item=clothes, cart=cart).exists():
        cart1 = get_object_or_404(CartClothes,item=clothes)
        amount = cart1.amount + 1
        total = real_pay * amount
        CartClothes.objects.filter(item=clothes).update(
            amount= amount,
            total = total
        )
        
    else:
        amount = 1 
        total = real_pay 
        cart_clothes = CartClothes.objects.create(
            item = clothes,
            cart=cart,
            amount=amount,
            total= total
        )
        
        cart_clothes.save()
        
    return HttpResponseRedirect('/home')

def view_cart(request):
    cus = get_object_or_404(Customer, uid=request.user)
    cart = get_object_or_404(Cart, customer=cus)
    cart_clothes = CartClothes.objects.filter(cart=cart)
    cart_electro = CartElectro.objects.filter(cart=cart)
    cart_book = CartBook.objects.filter(cart=cart)
    clothes = []
    electros = []
    books = []
    total = 0
    amount = len(cart_clothes) + len(cart_book) + len(cart_electro)
    for i in cart_clothes:
        clothes.append(i)
        if i.item.sale_off != 0:
            total = total + (i.item.price * i.item.sale_off * i.amount)/100
        else: total += i.item.price * i.amount
        
    for i in cart_electro:
        clothes.append(i)
        if i.item.sale_off != 0:
            total = total + (i.item.price * i.item.sale_off * i.amount)/100
        else: total += i.item.price * i.amount
        
    for i in cart_book:
        clothes.append(i)
        if i.item.sale_off != 0:
            total = total + (i.item.price * i.item.sale_off * i.amount)/100
        else: total += i.item.price * i.amount
   
    return render(request, "cart.html", {
        'amount': amount,
        'clothes': clothes,
        'electros': electros,
        'books': books,
        'total': total
    })
    
def delete_cart_clothes(request, id):
    cart_clothes = get_object_or_404(CartClothes, id=id)
    cart_clothes.delete()

    return HttpResponseRedirect('/customers/view-cart')    
    
# def detail_clothes(request, id):
    
#     return render(request, "detail_clothes.html")

def get_receiver(request):
    cus = get_object_or_404(Customer, uid=request.user)
    cart= get_object_or_404(Cart, customer=cus)
    cart_clothes = CartClothes.objects.filter(cart=cart)
    cart_electro = CartElectro.objects.filter(cart=cart)
    cart_book = CartBook.objects.filter(cart=cart)
    amount = len(cart_clothes) + len(cart_book) + len(cart_electro)
    if request.method == 'POST':
        form = ReceiverForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            phone = request.POST['phone']
            house_number = request.POST['house_number']
            commune = request.POST['commune']
            district = request.POST['district']
            city = request.POST['city']
            note = request.POST['note']
            if Receiver.objects.filter(customer=cus).exists():
                Receiver.objects.filter(customer=cus).update(
                    name = name,
                    phone = phone,
                    house_number = house_number,
                    commune = commune,
                    district = district,
                    city = city,
                    note = note
                )
                
            else:
                receiver = Receiver.objects.create(
                    customer= cus,
                    name = name,
                    phone = phone,
                    house_number = house_number,
                    commune = commune,
                    district = district,
                    city = city,
                    note = note
                )
                receiver.save()
                
            return HttpResponseRedirect('/customers/get-payment-method')
    else:
        if Receiver.objects.filter(customer=cus).exists():
            receiver = get_object_or_404(Receiver, customer=cus)
            form = ReceiverForm(
                initial= {
                    'name' : receiver.name,
                    'phone': receiver.phone,
                    'house_number': receiver.house_number,
                    'commune': receiver.commune,
                    'district': receiver.district,
                    'city': receiver.city
                }
            )
        else:   
            form = ReceiverForm()

    return render(request, "confirm.html", {
        'form': form,
        'amount': amount
    })

PAYMENT_METHOD =[
    (0, 'Thanh toán khi nhận hàng'),
    (1, 'Thanh toán qua thẻ ngân hàng'),
    (2, 'Thanh toán qua ví momo ')
]
   
def order(request):
    cus = get_object_or_404(Customer, uid=request.user)
    cart = get_object_or_404(Cart, customer=cus)
    receiver = get_object_or_404(Receiver, customer=cus)
    cart_clothes = CartClothes.objects.filter(cart=cart)
    cart_electro = CartElectro.objects.filter(cart=cart)
    cart_book = CartBook.objects.filter(cart=cart)
    amount = len(cart_clothes) + len(cart_book) + len(cart_electro)
    product = ''
    ship = get_object_or_404(Shipment, commune=receiver.commune, district=receiver.district, city=receiver.city)
    payment_method = get_object_or_404(Payment, user=cus)
    fee_ship = ship.fee
    total = 0
    
    for i in cart_clothes:
        product += str(i.item) + ' x' + str(i.amount) +"\n"
        if i.item.sale_off != 0:
            total = total + (i.item.price * i.item.sale_off)/100
        else: total += i.item.price
        
    for i in cart_electro:
        product += str(i.item) + ' x' + str(i.amount) +"\n"
        if i.item.sale_off != 0:
            total = total + (i.item.price * i.item.sale_off)/100
        else: total += i.item.price
        
    for i in cart_book:
        product += str(i.item) + ' x' + str(i.amount) +"\n"
        if i.item.sale_off != 0:
            total = total + (i.item.price * i.item.sale_off)/100
        else: total += i.item.price
    
    into_money = total + ship.fee
        
    order = Order.objects.create(
        customer=receiver,
        product = product,
        total = total,
        ship = ship,
        into_money = into_money,
        payment_methods= payment_method.method
    )
    order.save()
    for i in cart_clothes:
        i.delete()
    for i in cart_electro:
        i.delete()
    for i in cart_book:   
        i.delete()
    return render(request,"bill.html",{
        'amount': amount,
        'name' : receiver.name,
        'phone': receiver.phone,
        'house_number': receiver.house_number,
        'commune': receiver.commune,
        'district': receiver.district,
        'city': receiver.city,
        'note': receiver.note,
        'total': total,
        'fee_ship':fee_ship,
        'into_money': into_money,
        'method': payment_method.method,
        'methods': PAYMENT_METHOD,
        'product': product
    })

def payment(request):
    cus= get_object_or_404(Customer, uid=request.user)
    cart= get_object_or_404(Cart, customer=cus)
    cart_clothes = CartClothes.objects.filter(cart=cart)
    cart_electro = CartElectro.objects.filter(cart=cart)
    cart_book = CartBook.objects.filter(cart=cart)
    amount = len(cart_clothes) + len(cart_book) + len(cart_electro)
    if request.method == 'POST':
        form = PaymentMethodForm(request.POST)
        if form.is_valid():
            method = request.POST['method']
            if Payment.objects.filter(user=cus).exists():
                Payment.objects.filter(user=cus).update(
                    method = method
                )
            else:
                payment = Payment.objects.create(
                    user=cus,
                    method = method
                )
                payment.save()
            return HttpResponseRedirect('/customers/order')   
    else:
        if Payment.objects.filter(user=cus).exists():
            payment = get_object_or_404(Payment, user=cus)
            form = PaymentMethodForm(
                initial={
                    'method': payment.method
                }
            )
        else:
            form = PaymentMethodForm()
        
    return render(request, "payment_method.html", {
        'form': form, 
        'methods': PAYMENT_METHOD,
        'amount': amount
    })