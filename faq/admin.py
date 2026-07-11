from django.contrib import admin

from faq.models import FAQ

# Register your models here.


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'created_at')
    search_fields = ('question', 'answer')
    ordering = ('created_at',)

