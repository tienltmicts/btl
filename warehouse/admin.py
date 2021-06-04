from django.contrib import admin
from .models import *

# Register your models here.
class ClothesAdmin(admin.ModelAdmin):
    list_display = ('idProduct', 'name', 'color', 'size','amount', 'sold','inventory', 'entry_price', 'added_date', 'category', 'brand', 'origin')
    search_fields = ['idProduct', 'name', 'color', 'size','amount', 'sold','inventory', 'entry_price', 'added_date', 'category', 'brand', 'origin']

admin.site.register(Clothes, ClothesAdmin)

class ElectroAdmin(admin.ModelAdmin):
    list_display = ('idProduct', 'name', 'power','amount', 'sold','inventory', 'entry_price', 'added_date', 'category', 'brand', 'origin')
    search_fields = ['idProduct', 'name', 'power','amount', 'sold','inventory', 'entry_price', 'added_date', 'category', 'brand', 'origin']

admin.site.register(Electro, ElectroAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('idProduct', 'name', 'page_number', 'author', 'publishing_year','amount', 'sold','inventory', 'entry_price', 'added_date', 'category', 'brand', 'origin')
    search_fields = ['idProduct', 'name', 'page_number', 'author', 'publishing_year','amount', 'sold','inventory', 'entry_price', 'added_date', 'category', 'brand', 'origin']

admin.site.register(Book, BookAdmin)