from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
# Create your views here.

class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        kwargs.setdefault('view', self)
        if self.extra_context is not None:
            kwargs.update(self.extra_context)
        kwargs['slid_show'] = SlideShow.objects.all()
        return kwargs