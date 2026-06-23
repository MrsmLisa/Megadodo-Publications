from django.contrib import admin
from .models import Book 

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'category', 'sku')
    search_fields = ('title', 'author', 'category', 'sku')
    list_filter = ('category',)


admin.site.register(Book, BookAdmin)
