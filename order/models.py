from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models import F
# Create your models here.
from product.models import ShopProduct
user = get_user_model()

class Order(models.Model):
    user = models.ForeignKey(
        to=user,
        related_name='order_user',
        related_query_name='order_user',
        on_delete=models.CASCADE
    )
    description = models.TextField(
        verbose_name=_("description"),
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        verbose_name=_("created_at"),
        auto_now=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_("updated_at"),
        auto_now_add=True
    )

    class Meta:
        verbose_name = _("order")
        verbose_name_plural = _("orders")

    def __str__(self):
        return f'Order by {self.user}'

class Table(models.Model):
    order = models.ForeignKey(
        to=Order,
        related_name='table_order',
        related_query_name='table_order',
        on_delete=models.CASCADE
    )
    shop_product = models.ForeignKey(
        to=ShopProduct,
        related_name='table_shop_product',
        related_query_name='table_shop_product',
        on_delete=models.CASCADE
    )
    count = models.IntegerField(
        default=True
    )
    price = models.DecimalField(
        max_digits=1000000000,
        decimal_places=3
    )

    @property
    def summation(self):
        return F(self.count) * F(self.price)

    class Meta:
        verbose_name = _("table")
        verbose_name_plural = _("tables")

    def __str__(self):
        return f'Table for {self.order}'

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
        related_name="basket_item_basket",
        related_query_name="basket_items_basket",
        on_delete=models.CASCADE
    )
    shop_product = models.ForeignKey(
        to=ShopProduct,
        related_name="basket_item_shop_product",
        related_query_name="basket_item_shop_product",
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _("basket_item")
        verbose_name_plural = _("basket_items")

    def __str__(self):
        return f'basketItems for {self.basket}'

class payment(models.Model):
    order = models.OneToOneField(
        to=Order,
        related_name="payment_order",
        related_query_name="payment_order",
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        to=user,
        related_name="pyament_user",
        related_query_name="payment_user",
        on_delete=models.CASCADE
    )
    summation = models.DecimalField(
        max_digits=1000000000,
        decimal_places=3
    )

    class Meta:
        verbose_name = _("payment")
        verbose_name_plural = _("payments")

    def __str__(self):
        return f'payment for {self.order} by {self.user}'