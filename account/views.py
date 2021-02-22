from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.views.generic import FormView
from django.contrib.auth.views import LogoutView
from .form import SignUpForm, LoginForm
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

class Login(FormView):
    template_name = 'login.html'
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
