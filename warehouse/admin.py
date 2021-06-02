from django.contrib import admin
from .models import *

# Register your models here.
class ProducesAdmin(admin.ModelAdmin):
    list_display = ('idProduce', 'name', 'color', 'size','amount', 'sold','inventory', 'entry_price', 'added_date', 'category', 'brand', 'origin')
    search_fields = ['idProduce', 'name', 'color', 'size','amount', 'sold','inventory', 'entry_price', 'added_date', 'category', 'brand', 'origin']

admin.site.register(Produces, ProducesAdmin)