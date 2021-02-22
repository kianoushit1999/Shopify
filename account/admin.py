from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import *
from django.contrib.auth.forms import AdminPasswordChangeForm
# Register your models here.

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['email', 'phone', 'is_active']
    change_password_form = AdminPasswordChangeForm
    ordering = ('first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('email', 'phone')}),
        (_('Personal info'),
         {'fields': ('first_name', 'last_name', 'image')}),
        (_('Permissions'), {
            'classes': ('collapse',),
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
        ('More Info', {
            'classes': ('collapse', 'wide'),
            'fields': ('phone', 'first_name', 'last_name')
        }),
    )
    list_editable = ('phone',)

    inlines = []
    actions = ['staff_user', 'dis_staff', 'active_user', 'inactive_user']

    def staff_user(self, request, queryset):
        update = queryset.update(is_staff=True)
        self.message_user(
            request,
            _('%s getting staff') % update
        )

    staff_user.short_description = 'become draft'

    def dis_staff(self, request, queryset):
        update = queryset.update(is_staff=False)
        self.message_user(
            request,
            _('%s disable to be staff') % update
        )

    dis_staff.short_description = 'not staff'

    def active_user(self, request, queryset):
        update = queryset.update(is_staff=True)
        self.message_user(
            request,
            _('%s getting activate') % update
        )

    staff_user.short_description = 'active someone'

    def inactive_user(self, request, queryset):
        update = queryset.update(is_active=False)
        self.message_user(
            request,
            _('%s getting inactivate') % update
        )

    dis_staff.short_description = 'inactive someone'
@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('subject', 'body', 'user')
    search_fields = ('subject', 'user')
    list_filter = ('user',)
    list_display_links = ('user',)

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('city', 'street', 'zip_code', 'user')
    search_fields = ('city', 'user')
    list_filter = ('user',)
    list_display_links = ('user',)

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug', 'name', 'description')
    search_fields = ('slug', 'user', 'name')
    list_filter = ('user', )
    list_display_links = ('user', )
