from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Folder

def folder_detail(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id)
    parent_folder = folder.get_parent()
    child_folders = folder.get_children()
    
    return render(request, 'folders/folder_detail.html', {
        'folder': folder,
        'parent_folder': parent_folder,
        'child_folders': child_folders,
    })
