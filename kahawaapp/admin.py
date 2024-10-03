from django.contrib import admin
from .models import Kahawaapp

class KahawaappAdmin(admin.ModelAdmin):
    list_display = ("name","price", "image")




admin.site.register(Kahawaapp, KahawaappAdmin)
