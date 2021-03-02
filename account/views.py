from json import loads
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import resolve_url
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView, DetailView
from django.contrib.auth.views import LogoutView

from Shoppify import settings
from .form import SignUpForm, LoginForm
from order.models import *
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
        Basket.objects.create(user=user)
        return HttpResponseRedirect(self.get_success_url())


class Login(FormView):
    template_name = 'account/login.html'
    redirect_authenticated_user = True
    form_class = LoginForm
    model = User

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        data = self.get_form_kwargs().get('data')
        email = data.get('email')
        password = data.get('password')
        user = authenticate(email=email, password=password)
        print(self.get_success_url())
        if (user is not None and user.is_authenticated):
            login(self.request, user)
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect('/auth/login/')

    def get_success_url(self):
        if '=' in self.request.META.get('HTTP_REFERER'):
            return self.request.META.get('HTTP_REFERER').split('=')[1]
        return resolve_url(settings.LOGIN_REDIRECT_URL)


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
        kwargs["addresses"] = kwargs['object'].address_user
        kwargs["Redirect"] = 'false'
        kwargs['basket_items'] = {}
        kwargs['total'] = 0
        basket = Basket.objects.get(user=kwargs['object'])
        for item in basket.basket_basket_items.all():
            print(item.shop_product.price, item.counter)
            kwargs['basket_items'][f"{item.shop_product.shop.name}"] = [
                item.shop_product.products.name,
                item.counter,
                item.shop_product.price,
                item.shop_product.price * item.counter
            ]
            kwargs['total'] += (item.shop_product.price * item.counter)
        print(kwargs['basket_items'])
        print(kwargs['total'])
        return kwargs


@csrf_exempt
def update_info(request, pk):
    data = request.POST
    file = request.FILES
    user: User = User.objects.get(pk=pk)
    len_addr = len(data) - 4 if len(file) > 0 else len(data) - 5

    if file is not None:
        user.image = file.get('picture')
    first_name = data.get('first', '')
    last_name = data.get('last', '')
    email = data.get('email', '')
    phone = data.get('phone', None)

    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.phone = int(phone)

    response = {
        'first_name': first_name,
        'last_name': last_name,
        'address': [],
        'email': email,
        'phone': phone
    }

    for i in range(len_addr):
        addr = data.get('address' + str(i + 1))
        city, street, allay, zip_code = addr.split(',')
        response.get('address').append({
            'city': city,
            'street': street,
            'allay': allay,
            'zip_code': zip_code
        })
    user.save()
    return JsonResponse(data=response)


@csrf_exempt
def update_pass(request, pk):
    data = request.POST
    user: User = User.objects.get(pk=pk)
    old_pass = data.get('prevPass')
    new_pass = data.get('newPass')
    rep_pass = data.get('repPass')
    if (old_pass is not None and old_pass != '' and new_pass == rep_pass):
        if (user.check_password(old_pass)):
            try:
                user.set_password(new_pass)
                user.save()
                response = {
                    'response': 'ok'
                }
                return JsonResponse(data=response)
            except Exception as e:
                pass
    response = {
        'response': 'error'
    }
    return JsonResponse(data=response)


class Redirect(DetailView):
    template_name = 'account/personal_page.html'
    model = User
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        kwargs.setdefault('view', self)
        if self.extra_context is not None:
            kwargs.update(self.extra_context)
        kwargs["addresses"] = kwargs['object'].address_user
        kwargs["Redirect"] = 'true'
        kwargs['basket_items'] = {}
        kwargs['total'] = 0
        basket = Basket.objects.get(user=kwargs['object'])
        for item in basket.basket_basket_items.all():
            print(item.shop_product.price, item.counter)
            kwargs['basket_items'][f"{item.shop_product.shop.name}"] = [
                item.shop_product.products.name,
                item.counter,
                item.shop_product.price,
                item.shop_product.price * item.counter
            ]
            kwargs['total'] += (item.shop_product.price * item.counter)
        print(kwargs['basket_items'])
        print(kwargs['total'])
        return kwargs
