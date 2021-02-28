from django.conf.urls.static import static
from django.urls import path

from Shoppify import settings
from .views import *

app_name = 'account'

urlpatterns = [
                  path('signup/', SignUp.as_view(), name='sign_up'),
                  path('login/', Login.as_view(), name='login'),
                  path('logout/', Logout.as_view(), name='logout'),
                  path('person/<int:pk>/', PersonalPage.as_view(), name='personal_page'),
                  path('updatainfo/<int:pk>/', update_info, name='update_information'),
                  path('updatepass/<int:pk>/', update_pass, name='update_password'),
                  path('go_basket/<int:pk>/', Redirect.as_view(), name='go_basket')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
