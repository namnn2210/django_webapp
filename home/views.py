from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate, logout
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from course.views import get_courses_by_user


# Create your views here.
def home(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def show_profile(request):
    current_user = request.user
    current_user_courses = get_courses_by_user(request)
    return render(request, 'profile.html', {'current_user': current_user, 'current_user_courses': current_user_courses})
