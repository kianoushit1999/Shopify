from django.conf.urls.static import static
from django.urls import path

from Shoppify import settings
from .views import *

app_name = 'account'

urlpatterns = [
                  path('signup/', SignUp.as_view(), name='sign_up'),
                  path('login/', Login.as_view(), name='login'),
                  path('logout/', Logout.as_view(), name='logout')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
