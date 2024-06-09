from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.
def Register_Form(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.add_message(request, messages.SUCCESS, 'You have successfully registered')
            return redirect('login')
    else:
        register_form = RegisterForm()
    return render(request, 'signup.html', {'form': register_form, 'type': 'Register'})


def login_form(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username = user_name, password = user_pass)
            login(request, user)
            if user is not None:
                messages.add_message(request, messages.SUCCESS, 'Login successful')
                login(request, user)
                return redirect('profile')
            else:
                messages.add_message(request, messages.WARNING, 'Login unsuccessful')
                return redirect('register')
    else:
        login_form = AuthenticationForm()
    return render(request, 'signup.html', {'form': login_form, 'type': 'Login'})

def profile_view(request):
    return render(request, 'profile.html')