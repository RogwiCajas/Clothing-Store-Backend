
from django.http import JsonResponse
from django.views import View
#import de los modelos
from .models import Product
from .models import Address
from .models import Customer
from .models import Email
from .models import Order
from .models import Phone
from .models import ProductOrder
from .models import Shop
from .models import User

#import para manejo de los pk
from django.forms.models import model_to_dict


#Lista con todos los productos desde la base
class ProductosListView(View):
    def get(self, request):
        productos = Product.objects.all()
        return JsonResponse(list(productos.values()), safe=False)


#lista las direcciones 
class AddressListView(View):
    def get(self, request):
        address = Address.objects.all()
        return JsonResponse(list(address.values()), safe=False)
        
#lista las customer 
class CustomerListView(View):
    def get(self, request):
        customer = Customer.objects.all()
        return JsonResponse(list(customer.values()), safe=False)

#lista los email 
class EmailListView(View):
    def get(self, request):
        email = Email.objects.all()
        return JsonResponse(list(email.values()), safe=False)


#lista las ordenes 
class OrderListView(View):
    def get(self, request):
        order = Order.objects.all()
        return JsonResponse(list(order.values()), safe=False)

#lista de telefonos 
class PhoneListView(View):
    def get(self, request):
        phone = Phone.objects.all()
        return JsonResponse(list(phone.values()), safe=False)

#lista las ProductOrder 
class ProductOrderListView(View):
    def get(self, request):
        productorder = ProductOrder.objects.all()
        return JsonResponse(list(productorder.values()), safe=False)

#lista las shop 
class ShopListView(View):
    def get(self, request):
        Shop = Shop.objects.all()
        return JsonResponse(list(shop.values()), safe=False)

#lista las direcciones 
class UserListView(View):
    def get(self, request):
        user = User.objects.all()
        return JsonResponse(list(user.values()), safe=False)
        

#lista con un producto especificado en la url por el pk
#validar cuando el pk no existe
class ProductoView(View):
    def get(self, request, pk):
        producto = Product.objects.get(pk=pk)
        return JsonResponse(model_to_dict(producto))


class AddressView(View):
    def get(self, request, pk):
        address = Address.objects.get(pk=pk)
        return JsonResponse(model_to_dict(address))


class CustomerView(View):
    def get(self, request, pk):
        customer = Customer.objects.get(pk=pk)
        return JsonResponse(model_to_dict(customer))


class EmailView(View):
    def get(self, request, pk):
        email = Email.objects.get(pk=pk)
        return JsonResponse(model_to_dict(email))


        
class OrderView(View):
    def get(self, request, pk):
        order = Order.objects.get(pk=pk)
        return JsonResponse(model_to_dict(order))


        
class PhoneView(View):
    def get(self, request, pk):
        phone = Phone.objects.get(pk=pk)
        return JsonResponse(model_to_dict(phone))


           
class ProductOrderView(View):
    def get(self, request, pk):
        productorder = ProductOrder.objects.get(pk=pk)
        return JsonResponse(model_to_dict(productorder))

        
class ShopView(View):
    def get(self, request, pk):
        shop = Shop.objects.get(pk=pk)
        return JsonResponse(model_to_dict(shop))

        
class UserView(View):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        return JsonResponse(model_to_dict(user))


