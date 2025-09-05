from django.contrib import admin

from .models import Product, ServersLocations

@admin.register(ServersLocations)
class ServerLocationsAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'ping',
        'server_load',
        'is_active',
        'created_at',
        'updated_at',
    ]
    readonly_fields = [
        'created_at',
        'updated_at',
    ]
    list_filter = [
        'is_active',
    ]
    search_fields = [
        'name',
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'data_limit',
        'device_connections',
        'server_locations_count',
        'plan_price',
        'is_active',
        'created_at',
        'updated_at',
    ]
    readonly_fields = [
        'created_at',
        'updated_at',
    ]
    list_filter = [
        'is_active',
    ]
    search_fields = [
        'name',
    ]