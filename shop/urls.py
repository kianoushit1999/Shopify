from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from Shoppify import settings
from .views import *

app_name = 'shop'

urlpatterns = [
                  path('home/', Home.as_view(), name='home'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
