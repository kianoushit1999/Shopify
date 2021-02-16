from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'description')
    search_fields = ('user',)
    list_filter = ('user',)
    list_display_links = ('user',)

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('order', 'shop_product', 'price', 'summation')
    search_fields = ('order', 'shop_product')
    list_filter = ('order', 'shop_product')
    list_display_links = ('order', 'shop_product')

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user', )
    list_filter = ('user', )
    list_display_links = ('user', )

@admin.register(BasketItems)
class BasketItemsAdmin(admin.ModelAdmin):
    list_display = ('basket', 'shop_product')
    search_fields = ('basket', 'shop_product')
    list_filter = ('basket', 'shop_product')
    list_display_links = ('basket', 'shop_product')

@admin.register(payment)
class paymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'user', 'summation')
    search_fields = ('order', 'user')
    list_filter = ('order', 'user')
    list_display_links = ('user', 'order')