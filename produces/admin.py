from django.contrib import admin

from .models import *

# Register your models here.
class ItemClothesAdmin(admin.ModelAdmin):
    list_display = ('get_id', 'get_product', 'image','price', 'sale_off', 'describe',)
    search_fields = ['get_id', 'get_product', 'sale_off', 'price',]
    
    def get_id(self, obj):
        return obj.produce.idProduct
    get_id.short_description = 'Mã sản phẩm'
    
    def get_product(self, obj):
        return obj.produce
    get_product.short_description = 'Tên sản phẩm'

admin.site.register(ItemClothes, ItemClothesAdmin)

class ItemElectroAdmin(admin.ModelAdmin):
    list_display = ('get_id', 'get_product', 'image','price', 'sale_off', 'describe',)
    search_fields = ['get_id', 'get_product', 'sale_off', 'price',]
    
    def get_id(self, obj):
        return obj.produce.idProduct
    get_id.short_description = 'Mã sản phẩm'
    
    def get_product(self, obj):
        return obj.produce
    get_product.short_description = 'Tên sản phẩm'

admin.site.register(ItemElectro, ItemElectroAdmin)

class ItemBookAdmin(admin.ModelAdmin):
    list_display = ('get_id', 'get_product', 'image','price', 'sale_off', 'describe',)
    search_fields = ['get_id', 'get_product', 'sale_off', 'price',]
    
    def get_id(self, obj):
        return obj.produce.idProduct
    get_id.short_description = 'Mã sản phẩm'
    
    def get_product(self, obj):
        return obj.produce
    get_product.short_description = 'Tên sản phẩm'

admin.site.register(ItemBook, ItemBookAdmin)