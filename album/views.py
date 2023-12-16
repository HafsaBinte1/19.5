from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add_album(request):
    if request.method == 'POST':
        add_album_form = forms.AlbumForm(request.POST)
        if  add_album_form.is_valid():
            add_album_form.save()
            return redirect('add_album')
    
    else:
        add_album_form = forms.AlbumForm()


    return render(request, 'add_album.html',{'form':add_album_form})
