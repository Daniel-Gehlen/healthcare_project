# authentication/views.py
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')  # Redireciona para a página inicial após o registro
    else:
        form = UserRegistrationForm()
    return render(request, 'authentication/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redireciona para a página inicial após o login
        else:
            # Exiba uma mensagem de erro de login
            return render(request, 'authentication/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'authentication/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')  # Redireciona para a página inicial após o logout
