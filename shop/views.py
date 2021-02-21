from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from django.db.models import Q
from product.models import *


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
        kwargs['base_categories'] = BaseCategories.objects.all()
        kwargs['sample_product'] = Product.objects.filter(Q(category__name__iexact='Health') |
                                                          Q(category__name__iexact='cleaning') |
                                                          Q(category__name__iexact='Fitness'))
        kwargs['most_bought'] = ProductMeta.objects.order_by('-counter')[0:4]
        return kwargs
