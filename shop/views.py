from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from django.db.models import Q
from product.models import Category
# Create your views here.

class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        kwargs.setdefault('view', self)
        if self.extra_context is not None:
            kwargs.update(self.extra_context)
        kwargs['slid_show'] = SlideShow.objects.all()
        kwargs['categories'] = Category.objects.all()[0:9]
        kwargs['foods'] = Category.objects.filter(Q(parent__name__exact='foods&drink'))
        print(kwargs)
        return kwargs