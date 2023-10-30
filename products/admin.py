from django.contrib import admin

from products.models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'category', 'price',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)
