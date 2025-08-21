from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.Home, name='homesreen'),

     # register user
    path('register/',views.register, name='register'),

    # log in 
    path('login/',auth_views.LoginView.as_view(),name='login'),
]