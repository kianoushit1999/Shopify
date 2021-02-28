from json import loads
from django.http import JsonResponse
from product.views import *
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add_to_basket(request):
    data = loads(request.body)
    product_slug, shop_slug, shop_product_price, user_id = data.split()
    product = Product.objects.get(slug=product_slug)
    shop = Shop.objects.get(slug=shop_slug)
    user = User.objects.get(pk=int(user_id))
    shop_product = ShopProduct.objects.get(
        products=product,
        shop=shop,
        price=shop_product_price
    )
    print(shop_product)
    return JsonResponse(
        {
            'ans': 'ok'
        }
    )