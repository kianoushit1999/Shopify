from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models import F
# Create your models here.
from product.models import ShopProduct
user = get_user_model()

class Basket(models.Model):
    user = models.OneToOneField(
        to=user,
        related_name="basket_user",
        related_query_name="basket_user",
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _("basket")
        verbose_name_plural = _("baskets")

    def __str__(self):
        return f'Basket for {self.user}'


class BasketItems(models.Model):
    basket = models.ForeignKey(
        to=Basket,
        related_name="basket_basket_items",
        related_query_name="basket_basket_items",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    shop_product = models.ForeignKey(
        to=ShopProduct,
        related_name="basket_item_shop_product",
        related_query_name="basket_item_shop_product",
        on_delete=models.CASCADE
    )
    counter = models.IntegerField(
        default=True,
        null=True
    )

    class Meta:
        verbose_name = _("basket_item")
        verbose_name_plural = _("basket_items")

    def __str__(self):
        return f'basketItems for {self.basket}'