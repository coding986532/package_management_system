from csv import list_dialects
from django.contrib import admin
from .models import Installer

class InstallerAdmin(admin.ModelAdmin):
    list_display = ('Name','Date_Added')

admin.site.register(Installer, InstallerAdmin)
# Register your models here.
