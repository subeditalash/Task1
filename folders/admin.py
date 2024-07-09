from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Folder

class FolderAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name',)

admin.site.register(Folder, FolderAdmin)
