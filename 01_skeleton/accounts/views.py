from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST, require_safe, require_http_methods

# Create your views here.
def login(request):  #GET, POST
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movies:index')
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def logout(request):  #POST
    if request.method == "POST":
        auth_logout(request)
        return redirect('movies:index')
    return redirect('movies:index')


def signup(request):  #GET POST
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('movies:index')
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)


@require_POST
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('movies:index')


def update(request):
    pass
def password(request):
    pass
def profile(request):
    pass
def follow(request):
    pass