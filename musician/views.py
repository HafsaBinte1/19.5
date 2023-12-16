from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView, LogoutView
from . import forms
from django.shortcuts import render,redirect
from . import models
# # Create your views here.
# def add_musician(request):
#         if request.method == 'POST':
#             add_Musician_form = forms.MusicainForm(request.POST)
#             if add_Musician_form.is_valid():
#                 add_Musician_form.save()
#                 return redirect('add_musician')

#         else:
#             add_Musician_form = forms.MusicainForm()
            
#         return render(request, 'add_musician.html',{'form': add_Musician_form})



@method_decorator(login_required, name= 'dispatch')
class add_musician(CreateView):
    model = models.musician_model
    form_class = forms.MusicainForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('add_musician')

    def form_valid(self, form):
        form.instance.musician = self.request.user
        return super().form_valid(form)


class signup(CreateView):
     template_name = 'form.html'
     success_url = reverse_lazy('register')
     form_class = forms.RegistationForm

     def form_valid(self,form):
          response = super().form_valid(form)
          return response
     def get_context_data(self,**kwargs):
         context = super().get_context_data(**kwargs)
         context['type'] = 'Register'
         return context


class userlogin(LoginView):
    template_name = 'form.html'
    
    def get_success_url(self):
        return reverse_lazy('homepage')
    
    def form_valid(self, form):
        # form
        return super().form_valid(form)
    
    def form_invalid(self, form):
        # form
        return super().form_invalid(form)
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context

@method_decorator(login_required, name= 'dispatch')
class userlogout(LogoutView):
    template_name = 'logout.html'
    def get_success_url(self):
       return reverse_lazy('homepage')
    
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)

        return response