from django.contrib import admin
from .models import *

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('uid', 'name', 'email', 'birthday','phone', 'id_selfie','gender')

admin.site.register(Customer, CustomerAdmin)