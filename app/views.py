from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.views.decorators.cache import never_cache
from django.contrib.auth import logout


# from .models import Task
from .form import *
from .models import Note

@never_cache
def Home(request):  # main screen
    return render(request, 'index.html',{'section':'homescreen'})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the user object
            new_user.save()
            return render(request, 'registration/login.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    
    return render(request, 'registration/register.html', {'user_form': user_form})

@login_required
@never_cache
def editor_view(request):
    # Get or create note for user
    note, created = Note.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
    else:
        form = NoteForm(instance=note)

    return render(request, 'note.html', {'form': form})

# def auth_requere(request):
#     return render(auth_requere,'auth.html') 



def logout_view(request):
    # Log out and clear the session
    logout(request)

    # Redirect to homepage
    response = redirect('/')  

    response.delete_cookie('sessionid')

    # Clear cache 
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'

    return response
