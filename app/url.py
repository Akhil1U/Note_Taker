from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.Home, name='homesreen'),


     # register user
    path('register/',views.register, name='register'),
    path('note/',views.editor_view, name = 'homenote'),
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/',views.logout_view, name='logout'),

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