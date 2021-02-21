from django.db.models import Q, F
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import *


class SpecificCategory(TemplateView):
    template_name = 'category.html'

class OneProfuct(DetailView):
    template_name = 'single_product.html'
    model = Product

    def get_context_data(self, **kwargs):
        kwargs.setdefault('view', self)
        if self.extra_context is not None:
            kwargs.update(self.extra_context)
        product = kwargs['object']
        kwargs['images'] = Image.objects.filter(product__slug__iexact=product.slug)
        kwargs['cons'] = ConsProperty.objects.filter(product__slug__iexact=product.slug)
        kwargs['info'] = ProductMeta.objects.get(product__slug__iexact=product.slug)
        kwargs['shops'] = ShopProduct.objects.filter(products__slug__iexact=product.slug)
        kwargs['related'] = Product.objects.exclude(name=product.name)\
                                           .filter(Q(brand=product.brand) |
                                                   Q(category__exact=product.category))

        return kwargs