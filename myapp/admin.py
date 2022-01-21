from django.contrib import admin
from .models import ProductModel,CustomerModel,Cart,Order
# Register your models here.


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ["created_at", "photo", "p_des", "p_mode", "p_status", "p_occasion", "p_brand", "p_material", "p_type", "sell_price", "discounted_price", "discount", "og_price", "sub_cate", "main_cate", "name"][::-1]




@admin.register(CustomerModel)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ["state", "zipcode", "city", "locality", "email", "mobile", "name", "user"][::-1]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["size", "quantity", "product", "user"][::-1]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["status", "order_date","psize", "quantity", "product", "customer", "user"][::-1]


