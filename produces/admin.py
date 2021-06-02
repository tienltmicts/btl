from django.contrib import admin

from .models import *

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('get_id', 'get_produce', 'image','price', 'sale_off', 'describe',)
    search_fields = ['get_id', 'get_produce', 'sale_off', 'price',]
    
    def get_id(self, obj):
        return obj.produce.idProduce
    get_id.short_description = 'Mã sản phẩm'
    
    def get_produce(self, obj):
        return obj.produce
    get_produce.short_description = 'Tên sản phẩm'

admin.site.register(Item, ItemAdmin)