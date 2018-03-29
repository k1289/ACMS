from django.contrib import admin

# Register your models here.
from .models import Products, Service_Centres

admin.site.register(Products)
admin.site.register(Service_Centres)