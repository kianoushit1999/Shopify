from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from Shoppify import settings
from .views import *

urlpatterns = [
                  path('home/', Home, 'home'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
