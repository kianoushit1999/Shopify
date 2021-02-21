from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
# Create your views here.


class SignUp(FormView):
    template_name = 'sign_up.html'

class Login(LoginView):
    template_name = 'login.html'

class Logout(LogoutView):
    template_name = 'logout.html'
