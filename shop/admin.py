from django.contrib import admin
from .models import Product, Contact, Orders
# Register your models here.\


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "product_id",
        "product_name",
        "category",
        "subcategory",
        "pub_date"
    )


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'msg_id',
        'name',
        'email',
        'cell'
    )


class OrdersAdmin(admin.ModelAdmin):
    list_display = (
        'order_id',
        'name',
        'email',
        'phone'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Orders, OrdersAdmin)
