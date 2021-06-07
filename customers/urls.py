from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('add-cart-clothes/<int:id>/', views.add_cart_clothes, name="add_cart_clothes"),
    path('view-cart/', views.view_cart, name="view_cart"),
    path('delete-cart-clothes/<int:id>/', views.delete_cart_clothes, name="delete_cart_clothes"),
    path('get-receiver/', views.get_receiver, name="get_receiver"),
    path('get-payment-method/', views.payment, name="payment"),
    path('order/', views.order, name="order"),
]