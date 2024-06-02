from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'usuario_app/register.html', {'form': form})

def login_view(request):
    return render(request, 'usuario_app/login.html')

def home(request):
    return render(request, 'usuario_app/home.html')
