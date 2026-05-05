from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Manufacturer, Car, Driver

# Register your models here.

admin.site.register(Manufacturer)
admin.site.register(Car)
admin.site.register(Driver, UserAdmin)
