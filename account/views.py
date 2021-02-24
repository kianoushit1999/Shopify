from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.views.generic import FormView, DetailView
from django.contrib.auth.views import LogoutView
from .form import SignUpForm, LoginForm
from .models import *

class SignUp(FormView):
    template_name = 'account/signup.html'
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

class Login(FormView):
    template_name = 'account/login.html'
    redirect_authenticated_user = True
    success_url = '/home/'
    form_class = LoginForm
    model = User

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        data = self.get_form_kwargs().get('data')
        email = data.get('email')
        password = data.get('password')
        user = authenticate(email=email, password=password)
        print(self.get_success_url())
        if(user is not None and user.is_authenticated ):
            login(self.request, user)
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect('/auth/login/')

class Logout(LogoutView):
    template_name = None


class PersonalPage(DetailView):
    template_name = 'account/personal_page.html'
    model = User
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        kwargs.setdefault('view', self)
        if self.extra_context is not None:
            kwargs.update(self.extra_context)
        kwargs["addresses"]=kwargs['object'].address_user
        return kwargs