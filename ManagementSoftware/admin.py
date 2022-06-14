from django.contrib import admin
from .models import (
    Client,
    Site,
    Supplier,
    Article,
    Order,
)


# admin.site.register(Client)
# admin.site.register(Site)
# admin.site.register(Supplier)
# admin.site.register(Article)
# admin.site.register(Order)


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ("name",)


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'client_id']
    list_filter = ("name",)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ("name",)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'supplier_id', 'measurement_unit']
    list_filter = ("name",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'status', 'quantity', 'article_id', 'site_id', 'suppliers', 'clients']
    list_filter = ("status",)
