from django.contrib import admin

# Register your models here.
from .models import *
from .forms import *


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm

    list_display = ('name', 'price', 'old_price', 'created_at', 'updated_at', )
    list_display_links = ('name', )
    list_per_page = 50
    ordering = ['-created_at']
    search_fields = ['name', 'description','meta_keywords', 'meta_descriptions']
    exclude = ('created_at', 'updated_at')

    prepopulated_fields = {'slug':('name',)}



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['-created_at']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_descriptions']
    exclude = ('created_at', 'updated_at',)

    prepopulated_fields = {'slug':('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)