from django.contrib import admin
from gestionPedidos.models import User, Customer, Category, Address, Order, Phone, Product, ProductOrder, Email, Shop

# Register your models here.

class AdminAddress(admin.ModelAdmin):
    list_display=("address_id","address_country", "address_province", "address_city", "address_street" )
    search_fields=("address_province", "address_city","address_country")

class AdminCustomer(admin.ModelAdmin):
    list_display=("customer_id", "customer_FirstName", "customer_LastName")
    search_fields=("customer_id", "customer_FirstName", "customer_LastName")


class AdminCategory(admin.ModelAdmin):
    list_display=("category_id", "category_name", "category_description")
    search_fields=("category_id", "category_name", "category_description")

class AdminShop(admin.ModelAdmin):
    list_display=("shop_id", "shop_name", "shop_description")
    search_fields=("shop_id", "shop_name", "shop_description")


class AdminProduct(admin.ModelAdmin):
    list_display=("product_id", "product_name", "product_description")
    search_fields=("product_id", "product_name", "product_description")


class AdminOrder(admin.ModelAdmin):
    list_display=("order_id", "order_date", "order_amount", "order_descount")
    search_fields=("order_id", "order_date", "order_amount", "order_descount")
    date_hierarchy= "order_date"

admin.site.register(User)
admin.site.register(Address,AdminAddress)
admin.site.register(Customer,AdminCustomer)
admin.site.register(Category,AdminCategory)
admin.site.register(Shop,AdminShop)
admin.site.register(Order,AdminOrder)
admin.site.register(Phone)
admin.site.register(Email)
admin.site.register(Product,AdminProduct)
admin.site.register(ProductOrder)
