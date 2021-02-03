
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

#import de los modelos
from .models import Product
from .models import Address
from .models import Customer
from .models import Category
from .models import Email
from .models import Order
from .models import Phone
from .models import ProductOrder
from .models import Shop
from .models import User
from .models import Test
#import para manejo de los pk
from django.forms.models import model_to_dict

from rest_framework import viewsets
from .serializers import ProductSerilizer
from .serializers import ProductOrderSerilizer
from .serializers import PhoneSerilizer
from .serializers import AddressSerilizer
from .serializers import CategorySerilizer
from .serializers import CustomerSerilizer
from .serializers import EmailSerilizer
from .serializers import OrderSerilizer
from .serializers import ShopSerilizer
from .serializers import UserSerilizer





#metodos usando el apistest de django
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerilizer
    queryset = User.objects.all()

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerilizer
    queryset = Product.objects.all()

class ProductOrderViewSet(viewsets.ModelViewSet):
    serializer_class = ProductOrderSerilizer
    queryset = ProductOrder.objects.all()


class PhoneViewSet(viewsets.ModelViewSet):
    serializer_class = PhoneSerilizer
    queryset = Phone.objects.all()

class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerilizer
    queryset = Address.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerilizer
    queryset = Category.objects.all()

class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerilizer
    queryset = Customer.objects.all()

class EmailViewSet(viewsets.ModelViewSet):
    serializer_class = EmailSerilizer
    queryset = Email.objects.all()

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerilizer
    queryset = Order.objects.all()

class ShopViewSet(viewsets.ModelViewSet):
    serializer_class = ShopSerilizer
    queryset = Shop.objects.all()







'''
#Lista con todos los productos desde la base
class ProductosListView(View):
    def get(self, request):
        productos = Product.objects.all()
        print(productos)
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
'''

#norelacional
from mongoengine.queryset.queryset import QuerySet
import json
class TestView(View):
    def get(self, request):
        test = Test.objects
        query = test.to_json()
        dicts = json.loads(query)
        
        return JsonResponse(dicts, safe=False)
#usuario
#retorna el usuario con dicho pk

class UserView(View):
    @csrf_exempt
    def post(self, request):
        #user_id = request.POST["user_id"]
        #user_password = request.POST["user_password"]
        #user = User.objects().get(user_password=user_password)
        #print(user)
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        user = body['user_id']
        passw = body['user_password'] 
        respuesta ={
            "logeado": False
        }
        try:
            log = User.objects.get(user_id=user,user_password=passw)
            respuesta["logeado"]= True
            
        except User.DoesNotExist:
            respuesta["logeado"] = False
        return JsonResponse(respuesta, safe=False)     
