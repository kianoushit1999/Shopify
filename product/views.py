from django.db.models import Q, F
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, DetailView
from json import loads
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
        kwargs['comments'] = Comment.objects.filter(product__slug__exact=product.slug)
        return kwargs
@csrf_exempt
def add_comment(request):
    data = loads(request.body)
    rate = 5 if data.get('like') == 'true' else 0
    text = data.get('comment_text')
    product_slug, author = data.get('user')
    user = User.objects.get(email=author)
    product = Product.objects.get(slug=product_slug)
    Comment.objects.create(text=text, rate=rate, product=product, user=user)
    return JsonResponse(data=data)