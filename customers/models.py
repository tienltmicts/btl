from warehouse.models import Electro
from produces.models import ItemBook, ItemClothes, ItemElectro
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
USER_PROFILE_GENDER_CHOICES = [
        (0, 'Khác'),
        (1, 'Nam'),
        (2, 'Nữ'),
    ]
class Customer(models.Model):
    class Meta:
        db_table = "customer"
        verbose_name = 'Customer'
        verbose_name_plural = 'Customer'
    uid = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    birthday = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=255)
    gender = models.PositiveSmallIntegerField( choices=USER_PROFILE_GENDER_CHOICES, default=0)
    id_selfie = models.ImageField(('Selfie'),upload_to="media/profile",default = 'media/profile/1.jpg')

    class Meta:
        db_table = "customer"
        verbose_name = 'Customer'
        verbose_name_plural = 'Customer'
        
class CommentClothes(models.Model):
    reviewer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )
    item = models.ForeignKey(
        ItemClothes,
        on_delete=models.CASCADE
    )
    content = models.TextField()
    review = models.IntegerField(default=0)
    
    class Meta:
        db_table = "comment_clothes"
        verbose_name = 'Đánh giá về quần áo'
        verbose_name_plural = 'Đánh giá về quần áo'
    
class CommentElectro(models.Model):
    reviewer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )
    item = models.ForeignKey(
        ItemElectro,
        on_delete=models.CASCADE
    )
    content = models.TextField()
    review = models.IntegerField(default=0)
    
    class Meta:
        db_table = "comment_electro"
        verbose_name = 'Đánh giá về đồ điện tử'
        verbose_name_plural = 'Đánh giá về đồ điện tử'
    
class CommentBook(models.Model):
    reviewer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )
    item = models.ForeignKey(
        ItemBook,
        on_delete=models.CASCADE
    )
    content = models.TextField()
    review = models.IntegerField(default=0)
    
    class Meta:
        db_table = "comment_book"
        verbose_name = 'Đánh giá về sách'
        verbose_name_plural = 'Đánh giá về sách'
   
class LikeClothes(models.Model):
    item = models.ForeignKey(
        ItemClothes,
        on_delete=models.CASCADE
    )
    like = models.BigIntegerField()
    
    class Meta:
        db_table = "like_clothes"
        verbose_name = 'Yêu thích quần áo'
        verbose_name_plural = 'Yêu thích quần áo'

class LikeElectro(models.Model):
    item = models.ForeignKey(
        ItemElectro,
        on_delete=models.CASCADE
    )
    like = models.BigIntegerField()
    
    class Meta:
        db_table = "like_electro"
        verbose_name = 'Yêu thích đồ điện tử'
        verbose_name_plural = 'Yêu thích đồ điện tử'
        
class LikeBook(models.Model):
    item = models.ForeignKey(
        ItemBook,
        on_delete=models.CASCADE
    )
    like = models.BigIntegerField()
    
    class Meta:
        db_table = "like_book"
        verbose_name = 'Yêu thích sách'
        verbose_name_plural = 'Yêu thích sách'
        
class Cart(models.Model):
    customer = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE
    )
    nameCart = models.CharField(max_length=255,null=True, blank=True)
    
    class Meta:
        db_table = "cart"
        verbose_name = 'Giỏ hàng'
        verbose_name_plural = 'Giỏ hàng'
        
    def __str__(self):
        return str(self.customer)+"_"+ str(self.id)
    

class CartClothes(models.Model):
    item = models.ForeignKey(
        ItemClothes,
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    amount =  models.IntegerField(default=0)
    total = models.BigIntegerField(null=True, blank=True)
    
    class Meta:
        db_table = "clothes_cart"
        verbose_name = 'Giỏ hàng quần áo'
        verbose_name_plural = 'Giỏ hàng quần áo'
    
    
class CartElectro(models.Model):
    item = models.ForeignKey(
        ItemElectro,
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    amount =  models.IntegerField(default=0)
    total = models.BigIntegerField(null=True, blank=True)
    
    class Meta:
        db_table = "cart_electro"
        verbose_name = 'Giỏ hàng điện tử'
        verbose_name_plural = 'Giỏ hàng điện tử'
    
class CartBook(models.Model):
    item = models.ForeignKey(
        ItemBook,
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    amount =  models.IntegerField(default=0)
    total = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = "cart_book"
        verbose_name = 'Giỏ hàng sách'
        verbose_name_plural = 'giỏ hàng sách'
    

class Receiver(models.Model):
    customer = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255)
    commune = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    note = models.TextField(null=True, blank=True)
    
    class Meta:
        db_table = "receiver"
        verbose_name = 'Người nhận'
        verbose_name_plural = 'Người nhận'
    
class Shipment(models.Model):
    commune = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    fee = models.BigIntegerField(null=True, blank=True)
    
    class Meta:
        db_table = "shipment"
        verbose_name = 'Vận chuyển'
        verbose_name_plural = 'Vận chuyển'
        
    def __str__(self):
        return str(self.fee) +"đ"
        
class Order(models.Model):
    customer = models.ForeignKey(
        Receiver,
        on_delete=models.CASCADE
    )
    total = models.BigIntegerField(null=True, blank=True)
    product = models.TextField(null=True, blank=True)
    ship = models.ForeignKey(
        Shipment,
        on_delete=models.CASCADE
    )
    into_money = models.BigIntegerField(null=True, blank=True)
    payment_methods = models.CharField(max_length=255)
    
    class Meta:
        db_table = "order"
        verbose_name = 'Đặt hàng'
        verbose_name_plural = 'Đặt hàng'
    
PAYMENT_METHOD =[
    (0, 'Thanh toán khi nhận hàng'),
    (1, 'Thanh toán qua thẻ ngân hàng'),
    (0, 'Thanh toán qua ví momo ')
]

class Payment(models.Model):
    user = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    method = models.PositiveSmallIntegerField( choices=PAYMENT_METHOD, default=0)

    class Meta:
        db_table = "payment"
        verbose_name = 'Thanh toán'
        verbose_name_plural = 'Thanh toán'
    
    