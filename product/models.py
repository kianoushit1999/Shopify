from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.db import models
from account.models import Shop
from django.core.validators import MaxValueValidator, MinValueValidator
from statistics import mean
User = get_user_model()
# Create your models here.

class Category(models.Model):
    name = models.CharField(
        max_length=128,
        blank=True,
        verbose_name=_("name")
    )
    slug = models.SlugField(
        blank=True,
        null=True,
        db_index=True
    )
    details = models.TextField(
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to='product/product',
        null=True
    )
    parent = models.ForeignKey(
        to='self',
        on_delete=models.SET_NULL,
        related_name='category_parent',
        related_query_name='category_parent',
        verbose_name=_('parent'),
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(
        max_length=128,
        blank=True,
        verbose_name=_("name")
    )

    details = models.TextField(
        blank=True,
        null=True
    )

    image = models.ImageField(
        upload_to="product/brand/",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _('brand')
        verbose_name_plural = _('brands')

    def __str__(self):
        return self.name

class Product(models.Model):
    brand = models.ForeignKey(
        to=Brand,
        on_delete=models.CASCADE,
        related_name='product_brand',
        related_query_name='product_brand',
        verbose_name=_('brand'),
        null=True,
        blank=True
    )
    slug = models.SlugField(
        blank=True,
        null=True,
        db_index=True
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        related_name='product_category',
        related_query_name='product_category',
        verbose_name=_('category'),
        null=True,
        blank=True
    )
    name = models.CharField(
        max_length=128,
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to='product/product',
        null=True
    )
    details = models.TextField(
        blank=True,
        null=True,
    )

    @property
    def calc_rate(self):
        rates = list(self.comment_product.values_list('rate', flat=True))
        return mean(rates)

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def __str__(self):
        return f"product: {self.name}"


class ConsProperty(models.Model):
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    cons = models.CharField(
        max_length=255,
        verbose_name=_('cons')
    )

    def __str__(self):
        return self.cons


class Comment(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='comment_user',
        related_query_name='comment_user',
        verbose_name=_('user'),
        null=True,
        blank=True
    )
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name='comment_product',
        related_query_name='comment_product',
        verbose_name='product',
        null=True,
        blank=True
    )
    text = models.TextField(
        blank=True,
        null=True
    )
    rate = models.IntegerField(
        default=True,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )
    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')

    def __str__(self):
        return f'comment : {self.text}'

class Image(models.Model):
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name='Image_product',
        related_query_name='image_product',
        verbose_name=_('product'),
        null=True,
        blank=True
    )
    image = models.ImageField(
        upload_to='product/image/',
        null=True
    )
    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')

class ProductMeta(models.Model):
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name='product_meta_product',
        related_query_name='product_meta_product',
        verbose_name=_('product'),
        null=True,
        blank=True
    )
    label = models.CharField(
        max_length=128,
        blank=True,
        null=True
    )
    value = models.DecimalField(
        max_digits=1000000000,
        decimal_places=3
    )

    counter = models.IntegerField(
        default=0
    )

class Like(models.Model):
    user = models.ForeignKey(
        to=User,
        related_name="like_user",
        related_query_name="like_user",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    product = models.ForeignKey(
        to=Product,
        related_name="like_product",
        related_query_name="like_product",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _("like")
        verbose_name_plural = _("likes")

class Shop(models.Model):
    name = models.CharField(_('shop_name'), max_length=100)
    slug = models.SlugField(_('slug'), db_index=True, unique=True)
    description = models.TextField(_('description'), blank=True)
    image = models.ImageField(upload_to='images/shop', null=True, blank=True)
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='shops',
        related_query_name='shops_q',
    )

    class Meta:
        verbose_name = 'shop'
        verbose_name_plural = 'shops'

    def __str__(self):
        return f'shop name is {self.name}'

class ShopProduct(models.Model):
    shop = models.ForeignKey(
        to=Shop,
        on_delete=models.CASCADE,
        related_name='shop_product_shop',
        related_query_name='shop_product_shop',
        verbose_name=_('shop'),
        null=True,
        blank=True
    )

    products = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name='shop_product_products',
        verbose_name=_('products'),
        null=True,
        blank=True
    )

    price = models.IntegerField(
        verbose_name=_('price'),
        default=True
    )

    quality = models.IntegerField(
        verbose_name=_('quality'),
        default=True
    )

    class Meta:
        verbose_name = _('shop_product')
        verbose_name_plural = _('shop_products')

    def __str__(self):
        return f'shopProduct {self.shop}'