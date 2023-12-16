from django.utils.decorators import method_decorator
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from album.forms import AlbumForm
from album.models import album_model
from musician.models import musician_model
from django.urls import reverse_lazy
from django.views import generic
from musician.forms import MusicainForm

class home(generic.ListView):
    model = album_model
    template_name = 'home.html'
    context_object_name = 'data'


# def edit_post(request, id):
#     postOfAlbum = album_model.objects.get(pk=id) 
#     post_formofalbum = AlbumForm(instance=postOfAlbum)
    
#     if request.method == 'POST': 
#         post_form_album = AlbumForm(request.POST, instance=postOfAlbum) 
#         if post_form_album.is_valid(): 
#             post_form_album.save() 
#             return redirect('homepage')
#     else:
#         post_form_album = AlbumForm(instance=postOfAlbum) 
        

#     return render(request, 'edit.html', {'form' : post_form_album})


@method_decorator(login_required, name= 'dispatch')
class edit_post(generic.UpdateView):
    model = album_model
    form_class = AlbumForm
    template_name = 'edit.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')


# def edit_post_musician(request, id):
#     postOfmusician = musician_model.objects.get(pk=id) 
#     post_formoMusicain = MusicainForm(instance=postOfmusician)
    
#     if request.method == 'POST': 
#         post_form_musicain = MusicainForm(request.POST, instance=postOfmusician) 
#         if post_form_musicain.is_valid(): 
#             post_form_musicain.save() 
#             return redirect('homepage')
#     else:
#         post_form_musicain = MusicainForm(instance=postOfmusician) 
        

#     return render(request, 'edit.html', {'form' : post_form_musicain})


@method_decorator(login_required, name= 'dispatch')
class edit_post_musician(generic.UpdateView):
    model = musician_model
    form_class = MusicainForm
    template_name = 'edit.html'
    pk_url_kwarg ='id'
    success_url = reverse_lazy('homepage')



# def delete_post(request, id):
#     postOfAlbum = musician_model.objects.get(pk=id) 
#     postOfAlbum.delete()
#     return redirect('homepage')
    
@method_decorator(login_required, name= 'dispatch')
class delete_post(generic.DeleteView):
    model = album_model
    template_name = 'delete.html'
    success_url = reverse_lazy('homepage')
    pk_url_kwarg = 'id'