from django.core.exceptions import ImproperlyConfigured
from django.db.models import Q, F, QuerySet
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView
from json import loads
from .models import *


class SpecificCategories(ListView):
    template_name = 'category.html'
    model = Product
    template_name_suffix = ''

    def get_queryset(self):
        self.category_slug = self.kwargs['slug']
        """
        Return the list of items for this view.
        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        if self.queryset is not None:
            queryset = self.queryset
            if isinstance(queryset, QuerySet):
                queryset = queryset.all()
        elif self.model is not None:
            queryset = Product.objects.filter(category__slug=self.kwargs['slug'])
        else:
            raise ImproperlyConfigured(
                "%(cls)s is missing a QuerySet. Define "
                "%(cls)s.model, %(cls)s.queryset, or override "
                "%(cls)s.get_queryset()." % {
                    'cls': self.__class__.__name__
                }
            )
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)
        return queryset

    def get_context_data(self, **kwargs):
        kwargs.setdefault('view', self)
        if self.extra_context is not None:
            kwargs.update(self.extra_context)

        kwargs['products'] = Product.objects.filter(category__slug=self.category_slug)
        kwargs['brands'] = []
        kwargs['shops'] = []
        kwargs['product_brand'] = {}
        for object in Brand.objects.all():
            if object.product_brand.filter(category__slug=self.category_slug):
                kwargs['brands'].append(object)
                if kwargs['product_brand'].get(object.name, None) is None:
                    kwargs['product_brand'][object.name] = ""


        for product in Product.objects.filter(category__slug=self.category_slug):
            for shop_product in product.shop_product_products.all():
                kwargs['shops'].append(shop_product.shop)
                kwargs['product_brand'][product.brand.name] = (kwargs['product_brand'][product.brand.name] +' '+ shop_product.shop.name)
        return kwargs

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
        kwargs['satisfaction_product'] = int(product.calc_rate*20)
        return kwargs
@csrf_exempt
def add_comment(request):
    data = loads(request.body)
    rate = 5 if data.get('like') == 'true' else 0
    text = data.get('comment_text').strip()
    product_slug, author = data.get('user')
    user = User.objects.get(email=author)
    product = Product.objects.get(slug=product_slug)
    Comment.objects.create(text=text, rate=rate, product=product, user=user)
    response = {
        'text': text,
        'user': user.first_name
    }
    return JsonResponse(data=response)