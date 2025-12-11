from django.contrib import admin
from .models import Category, Product, ContactLink

admin.site.register(Category)
admin.site.register(Product)

@admin.register(ContactLink)
class ContactLinkAdmin(admin.ModelAdmin):
    list_display = ['platform', 'url', 'display_text', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    list_filter = ['platform', 'is_active']
    search_fields = ['platform', 'url', 'display_text']