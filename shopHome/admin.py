from django.contrib import admin
from .models import *

# Register your models here.

class FashionAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "image")
admin.site.register(Fashion, FashionAdmin)


class ElectronicAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "image")
admin.site.register(Electronic, ElectronicAdmin)


class JewelleryAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "image")
admin.site.register(Jewellery, JewelleryAdmin)