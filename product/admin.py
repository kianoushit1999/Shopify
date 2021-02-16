from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent', 'image')
    search_fields = ('parent', 'name')
    list_filter = ('parent',)
    list_display_links = ('parent',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'details', 'image')
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('brand', 'slug', 'category', 'name')
    search_fields = ('brand', 'slug', 'category')
    list_filter = ('brand', 'category')
    list_display_links = ('brand', 'category')

@admin.register(ShopProduct)
class ShopProductAdmin(admin.ModelAdmin):
    list_display = ('shop', 'products', 'price', 'quality')
    search_fields = ('shop', 'products', 'quality')
    list_filter = ('shop', 'products')
    list_display_links = ('shop', 'products')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'rate', 'text')
    search_fields = ('user', 'product', 'rate')
    list_filter = ('user', 'product')
    list_display_links = ('user', 'product')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')
    search_fields = ('product',)
    list_filter = ('product',)
    list_display_links = ('product',)

@admin.register(ProductMeta)
class ProductMetaAdmin(admin.ModelAdmin):
    list_display = ('product', 'label', 'value')
    search_fields = ('label', 'value')
    list_filter = ('product',)
    list_display_links = ('product',)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('product', 'user')
    search_fields = ('user', 'product')
    list_filter = ('product', 'user')
    list_display_links = ('product', 'user')

@admin.register(Shop)
class Shop(admin.ModelAdmin):
    list_display = ('name', 'slug', 'user', 'description')
    search_fields = ('user', 'name', 'slug')
    list_filter = ('user',)
    list_display_links = ('user', )