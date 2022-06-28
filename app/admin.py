from django.contrib import admin
from .models import Talaba

# Register your models here.
class TalabaAdmin(admin.ModelAdmin):
    list_display = ['id','firstname','lastname','faculties','direction','stage','group']
admin.site.register(Talaba, TalabaAdmin)