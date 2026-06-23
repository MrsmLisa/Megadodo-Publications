from django.contrib import admin
from .models import Product, Category 

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'category', 'sku')
    search_fields = ('title', 'author', 'category', 'sku')
    list_filter = ('category',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
