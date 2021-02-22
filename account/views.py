from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .form import SignUpForm
from .models import User

class SignUp(FormView):
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = '/auth/login/'
    model = User

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        data = self.get_form_kwargs().get('data')
        email = data.get('email')
        phone = data.get('phone')
        password = data.get('password')
        user = User(email=email, phone=phone)
        user.set_password(password)
        user.save()
        return HttpResponseRedirect(self.get_success_url())

class Login(LoginView):
    template_name = 'login.html'

class Logout(LogoutView):
    template_name = None
