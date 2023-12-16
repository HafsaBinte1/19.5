"""
URL configuration for musiciansdirectory project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home.as_view(), name = 'homepage'),
    path('album/', include('album.urls')),
    path('musician/', include('musician.urls')),
    path('edit/<int:id>', views.edit_post.as_view(), name='edit_post'),
    path('delete/<int:id>', views.delete_post.as_view(), name='delete_post'),
    path('editMusician/<int:id>', views.edit_post_musician.as_view(), name='edit_post_musicain'),
]
