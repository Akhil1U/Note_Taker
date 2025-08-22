from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.Home, name='homesreen'),


     # register user
    path('register/',views.register, name='register'),
    path('note/',views.editor_view, name = 'homenote'),

    # log in 
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('authenticate/',)

    
     path('logout/',auth_views.LogoutView.as_view(template_name = 'registration/log_out.html'), name='logout'),


    # password change 

       path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    path(
        'password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='registration/password_change_done.html'
        ),
        name='password_change_done'
    ),








]