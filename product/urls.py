from django.conf.urls.static import static
from django.urls import path

from Shoppify import settings
from .views import *

app_name = 'product'
urlpatterns = [
                    path('<slug:slug>/', SpecificCategory.as_view(), name='category'),
                    path('<slug:slug>/', OneProfuct.as_view(), name='singleProduct')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
