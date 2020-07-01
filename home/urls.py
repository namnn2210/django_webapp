from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.user_logout, name='logout'),
    path('profile', views.show_profile, name='profile')
]
