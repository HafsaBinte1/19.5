from django import forms
from .models import album_model

class AlbumForm(forms.ModelForm):
    class Meta:
        model = album_model
        fields = '__all__'
