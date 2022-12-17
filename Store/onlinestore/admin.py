from django.contrib import admin

from .models import Product, Order, OrderItem, ShippingAdress


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'price',
                    'colors',
                    'sizes',
                    )
    list_editable = ('price', 'colors', 'sizes', )
    search_fields = ('name', 'price', 'colors', 'sizes', )
    list_filter = ('name', 'price', 'colors', 'sizes', )
    empty_value_display = '-пусто-'


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product',
                    'order',
                    'quantity',
                    'date_added',
                    )
    list_editable = ('order', 'quantity', )
    search_fields = ('product', 'order', 'quantity', 'date_added', )
    list_filter = ('product', 'order', 'quantity', 'date_added', )
    empty_value_display = '-пусто-'


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer',
                    'data_order',
                    'complete',
                    'transaction_id',
                    )
    search_fields = ('customer', 'data_order', 'complete', 'transaction_id', )
    list_filter = ('customer', 'data_order', 'complete', 'transaction_id', )
    empty_value_display = '-пусто-'


class ShippingAdressAdmin(admin.ModelAdmin):
    list_display = ('customer',
                    'order',
                    'state',
                    'city',
                    'adress',
                    'date_added'
                    )
    search_fields = ('customer', 'order', 'state', 'city', 'adress', 'date_added')
    list_filter = ('customer', 'order', 'state', 'city', 'adress', 'date_added')
    empty_value_display = '-пусто-'


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAdress, ShippingAdressAdmin)