from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Category)
class CategoryAdmin(DjangoMpttAdmin):
    # list_display = ['title', 'slug', 'available', 'created', 'updated']
    # list_filter = ['available', 'created', 'updated']
    # list_editable = ['available']
    prepopulated_fields = {"slug": ("title",)}
