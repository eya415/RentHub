# admin.py
# type: ignore
from django.contrib import admin
from .models import Product, Category, Brand, WishlistItem
from .models import Order, OrderItem



from .models import IndividualProfile, CorporateProfile, StudioProfile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('created_at',)

@admin.register(IndividualProfile)
class IndividualProfileAdmin(ProfileAdmin):
    list_display = ProfileAdmin.list_display + ('full_name', 'professional_category')
    search_fields = ProfileAdmin.search_fields + ('full_name',)

@admin.register(CorporateProfile)
class CorporateProfileAdmin(ProfileAdmin):
    list_display = ProfileAdmin.list_display + ('company_name', 'ceo_name')
    search_fields = ProfileAdmin.search_fields + ('company_name', 'ceo_name')

@admin.register(StudioProfile)
class StudioProfileAdmin(ProfileAdmin):
    list_display = ProfileAdmin.list_display + ('studio_name',)
    search_fields = ProfileAdmin.search_fields + ('studio_name',)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'price')
    search_fields = ('name',)
    list_filter = ('brand', 'category')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(WishlistItem)
class WishlistItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'added_at')
    list_filter = ('user', 'added_at')
    search_fields = ('product__name', 'user__username')



@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price']
    list_filter = ['product']
    search_fields = ['order__user__username', 'product__name']


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0




class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'user', 'start_date', 'end_date', 
        'is_delivery', 'total_price', 'created_at', 'status'
    ]
    list_filter = ['is_delivery', 'start_date', 'end_date', 'status']
    search_fields = [
        'user__username', 'delivery_name', 
        'delivery_phone', 'delivery_address'
    ]
    date_hierarchy = 'created_at'
    inlines = [OrderItemInline]