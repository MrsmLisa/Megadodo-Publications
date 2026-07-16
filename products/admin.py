from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Product, Category

# Register your models here.


class ProductAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
    list_display = ('name', 'author', 'price', 'category', 'sku')
    search_fields = ('name', 'author', 'category', 'sku')
    list_filter = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
