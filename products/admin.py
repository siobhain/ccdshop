from django.contrib import admin
from .models import Category, Collection, Product

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'engravable',
        'sizeable',
    )


class CollectionAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'description',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'collection',
        'price',
        'sizeable',
        'image'
    )
    ordering = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Product, ProductAdmin)
