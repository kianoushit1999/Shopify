from json import loads

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
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
        if (user is not None and user.is_authenticated):
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
        kwargs["addresses"] = kwargs['object'].address_user
        return kwargs


@csrf_exempt
def update_info(request, pk):
    data = request.POST
    file = request.FILES
    user: User = User.objects.get(pk=pk)
    response = {
        'first_name': '',
        'last_name': '',
        'address': [],
        'email': '',
        'phone': ''
    }

    if file is not None:
        user.image = file.get('picture')
    first_name = data.get('first', [''])[0]
    last_name = data.get('last', [''])[0]
    email = data.get('email', [''])[0]
    phone = data.get('phone', [''])[0]

    print(request.POST.get('address'))
    print("*-*-*-*-*-*")
    print(data)
    print(len(file))
    #
    # user.first_name = first_name
    # user.last_name = last_name
    # user.email = email
    # user.phone = int(phone)
    # print(address)
    # print("*-*-*-*-*-*")
    # if len(address[0]) > 1:
    #     city, street, allay, zip_code = address[0].split(',')
    #     Address.objects.create(user=user, city=city, street=street, allay=allay, zip_code=int(zip_code))
    #     response.get('address')[0] = {
    #         'city': city,
    #         'street': street,
    #         'allay': allay,
    #         'zip_code': zip_code
    #     }
    # if len(address) > 1:
    #     for index, add in enumerate(address[1:]):
    #         print(add)
    #         city, street, allay, zip_code = add.split(',')
    #         Address.objects.create(user=user, city=city, street=street, allay=allay, zip_code=zip_code)
    #         response.get('address')[index + 1] = {
    #             'city': city,
    #             'street': street,
    #             'allay': allay,
    #             'zip_code': zip_code
    #         }
    # user.save()
    return JsonResponse(data=response)
