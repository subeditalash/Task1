# folders/admin.py
from django.contrib import admin
from .models import Folder

class FolderAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')

admin.site.register(Folder, FolderAdmin)
