from django import forms
from .models import musician_model
from  django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class MusicainForm(forms.ModelForm):
    class Meta:
        model = musician_model
        fields = '__all__'

class RegistationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email']