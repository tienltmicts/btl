from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('uid', 'name', 'email', 'birthday','phone', 'id_selfie','gender')

admin.site.register(Customer, CustomerAdmin)

class CommentClothesAdmin(admin.ModelAdmin):
    list_display = ('reviewer', 'item', 'content', 'review')

admin.site.register(CommentClothes, CommentClothesAdmin)

class CommentElectroAdmin(admin.ModelAdmin):
    list_display = ('reviewer', 'item', 'content', 'review')

admin.site.register(CommentElectro, CommentElectroAdmin)

class CommentBookAdmin(admin.ModelAdmin):
    list_display = ('reviewer', 'item', 'content', 'review')

admin.site.register(CommentBook, CommentBookAdmin)

class LikeClothesAdmin(admin.ModelAdmin):
    list_display = ( 'item', 'like')

admin.site.register(LikeClothes, LikeClothesAdmin)

class LikeElectroAdmin(admin.ModelAdmin):
    list_display = ( 'item', 'like')

admin.site.register(LikeElectro, LikeElectroAdmin)

class LikeBookAdmin(admin.ModelAdmin):
    list_display = ( 'item', 'like')

admin.site.register(LikeBook, LikeBookAdmin)

class CartClothesAdmin(admin.ModelAdmin):
    list_display = ( 'item', 'cart', 'amount', 'total')

admin.site.register(CartClothes, CartClothesAdmin)

class CartElectroAdmin(admin.ModelAdmin):
    list_display = ( 'item', 'cart', 'amount', 'total')

admin.site.register(CartElectro, CartElectroAdmin)

class CartBookAdmin(admin.ModelAdmin):
    list_display = ( 'item', 'cart', 'amount', 'total')

admin.site.register(CartBook, CartBookAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ( 'customer', 'nameCart', )
    
    def get_clothes(self, obj):
        return mark_safe("<br/>".join([str(m.item) for m in obj.clothes.all()]))
    get_clothes.short_description = 'Quần áo'
    
    def get_electros(self, obj):
        return mark_safe("<br/>".join([str(m.item) for m in obj.electros.all()]))
    get_electros.short_description = 'Đồ điện tử'
    
    def get_books(self, obj):
        return mark_safe("<br/>".join([str(m.item) for m in obj.books.all()]))
    get_books.short_description = 'Sách'

admin.site.register(Cart, CartAdmin)

class ShipmentAdmin(admin.ModelAdmin):
    list_display = ( 'commune', 'district', 'city', 'fee')
    
admin.site.register(Shipment, ShipmentAdmin)

class ReceiverAdmin(admin.ModelAdmin):
    list_display = ( 'customer','name','phone', 'house_number', 'commune', 'district', 'city', 'note')
    
admin.site.register(Receiver, ReceiverAdmin)