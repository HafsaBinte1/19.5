from django.urls import path,include
from . import views
urlpatterns = [
    path('add/',views.add_album,name='add_album')
]
