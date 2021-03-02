from json import loads
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from product.views import *
from .models import *
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@login_required(login_url='/auth/login/')
def add_to_basket(request):
    data = loads(request.body)
    product_slug, shop_slug, shop_product_price, user_id = data.split()
    print('*-----------------------*----------------------------*')
    print(user_id)
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
    product = Product.objects.get(slug=product_slug)
    shop = Shop.objects.get(slug=shop_slug)
    shop_product = ShopProduct.objects.get(
        products=product,
        shop=shop,
        price=shop_product_price
    )
    basket = Basket.objects.get(user__pk=int(user_id))
    if(len(BasketItems.objects.filter(basket=basket, shop_product=shop_product))==0):
        BasketItems.objects.create(basket=basket, shop_product=shop_product)
    else:
        basket_items = BasketItems.objects.get(basket=basket, shop_product=shop_product)
        basket_items.counter += 1
        basket_items.save()
    print(shop_product)
    return JsonResponse(
        {
            'ans': 'ok'
        }
    )