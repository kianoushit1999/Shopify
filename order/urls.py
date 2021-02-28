from django.conf.urls.static import static
from django.urls import path
from .views import *
from Shoppify import settings
from .views import *
app_name = 'order'

urlpatterns = [
                    path("add_basket/", add_to_basket, name="add_basket")
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
