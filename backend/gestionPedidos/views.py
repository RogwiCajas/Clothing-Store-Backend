
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

from django.db.models import Sum





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
    @csrf_exempt
    def get(self, request):
        test = Test.objects
        query = test.to_json()
        dicts = json.loads(query)
        
        return JsonResponse(dicts, safe=False)
    @csrf_exempt
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        id_usuario = body['id_usuario']
        detalle = body['detalle']
        test = Test(id_usuario=id_usuario, detalle=detalle)
        test.save()
        inserted ={
            'inserted': True
        }
        
        return JsonResponse(inserted)
    @csrf_exempt
    def update(self, request, id): #no testeada, probablemente no sirva y se caiga xdd
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        id_item= body['id_item']
        item_cant= body['item_cant']

        test = Test.objects.get(id_usuario=id)
        test.detalle[carrito][id_item][cantidad]= item_cant
        test.save()
        updated ={
            'updated': True
        }
        
        return JsonResponse(updated)
    @csrf_exempt
    def delete(self, request, id): #no testeada, borra por ide user
        
        test = Test.objects.get(id_usuario=id)
        test.delete()
        deleted ={
            'deleted': True
        }
        
        return JsonResponse(deleted)
#retorna el usuario con dicho pk
class UserView(View):
    @csrf_exempt
    def post(self, request):
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

class ActualizarPassword(View):
    @csrf_exempt
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        user = body['user_id']
        passwOld = body['user_password1'] 
        passwNew = body['user_password2'] 


        respuesta ={
            "Validacion": False

        }
        try:
            User.objects.get(user_id=user,user_password=passwOld)
            respuesta["Validacion"]= True
            User.objects.update(user_id=user,user_password=passwNew)
        except User.DoesNotExist:
            respuesta["Validacion"] = False
        return JsonResponse(respuesta, safe=False)

class TotalUser(View):
    @csrf_exempt
    def get(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        respuesta ={
            "Total": 0

        }
        try:
            contador = User.objects.all().count()
            respuesta["Total"]= contador
        except User.DoesNotExist:
            respuesta["Total"] = 0
        return JsonResponse(respuesta, safe=False)

class totalGanacia(View):
    @csrf_exempt
    def get(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        respuesta ={
            "Total": 0

        }
        try:
            amount = Order.objects.all().aggregate(Sum('order_amount'))
            discount = Order.objects.all().aggregate(Sum('order_descount'))
            respuesta["Total"]= amount['order_amount__sum'] -  discount['order_descount__sum']
            #respuesta["Total"]= amount
        except Order.DoesNotExist:
            respuesta["Total"] = 0
        return JsonResponse(respuesta, safe=False)

class OrdenesPorFecha(View):
    @csrf_exempt
    def get(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        respuesta ={

        }
        try:
            fecha = Order.objects.filter(date__year>'2021', 
                      date__month= "01")
            respuesta=fecha
        except Order.DoesNotExist:
            respuesta["Respuesta"] = 0
        return JsonResponse(respuesta, safe=False)


class totalGanaciaEstimada(View):
    @csrf_exempt
    def get(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        respuesta ={
            "Total": 0

        }
        try:
            amount = Order.objects.all().aggregate(Sum('order_amount'))
            discount = Order.objects.all().aggregate(Sum('order_descount'))
            respuesta["Total"]= amount['order_amount__sum'] -  discount['order_descount__sum']
            #respuesta["Total"]= amount
        except User.DoesNotExist:
            respuesta["Validacion"] = 0
        return JsonResponse(respuesta, safe=False)


class CrearCuenta(View):
    @csrf_exempt
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        user = body['user_id']
        passw = body['user_password']
        isAdmin = body['user_is_admin']
        nombre = body['customer_firstname'] 
        apellido = body['customer_lastname'] 
        pais = body['customer_country'] 
        ciudad = body['customer_city'] 
        direccion = body['customer_address'] 
        cedula = body['customer_id'] 
 
 

        respuesta ={
            "Creacion": False
        }
        try:
            User.objects.get(user_id=user)
            respuesta["Creacion"]= False
        except User.DoesNotExist:
            respuesta["Creacion"] = True
            usuario = User.objects.create(user_id=user,user_password=passw,user_is_admin=isAdmin)
            usuario.save()
            Customer.objects.create(user_id=user, customer_id=cedula, customer_FirstName=nombre, customer_LastName=apellido, customer_country= pais, customer_city=ciudad, customer_address=direccion)
        return JsonResponse(respuesta, safe=False)

class DatosUser(View):
    @csrf_exempt
    def get(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        user = body['user_id']
        

        respuesta ={
            "Creacion": False,
            "Customer_id"
            "Nombre": "",
            "Apellido": "",
            "Correo": "",
            "Telefono": "",
            "Pais": "",
            "Ciudad": ""
        }
        try:
            cliente = Custumer.objects.get(user_id=user)
            respuesta["Customer_id"]= cliente.get(cliente)
            respuesta["Creacion"]= True
        except User.DoesNotExist:
            respuesta["Creacion"] = False

        return JsonResponse(respuesta, safe=False)