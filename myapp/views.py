from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from .forms import SignUpForm, LogInForm


def index(request):
    return render(request, 'myapp/index.html')


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'myapp/register.html', {'form': form})


def Login(request):
    error = False
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('index')
            else:
                error = True
    else:
        form = LogInForm()

    return render(request, 'myapp/login.html', {'form': form, 'error': error})
