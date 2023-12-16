from django.urls import path,include
from . import views
urlpatterns = [
    path('add/',views.add_musician.as_view(),name='add_musician'),
    path('register/', views.signup.as_view(), name='register'),
    path('login/',views.userlogin.as_view(), name = 'login'),
    path('logout/',views.userlogout.as_view(), name = 'logout'),
]
