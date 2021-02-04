#Archivo creado para las urls de la api
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
'''
from .views import ProductosListView, ProductoView
from .views import AddressListView, AddressView
from .views import CustomerListView, CustomerView
from .views import EmailListView, EmailView
from .views import OrderListView, OrderView
from .views import PhoneListView, PhoneView
from .views import ProductOrderListView, ProductOrderView
from .views import ShopListView, ShopView
from .views import UserListView, UserView
'''
from .views import UserView
from .views import TestView
from .views import ActualizarPassword
from .views import CrearCuenta
from .views import TotalUser
from .views import totalGanaciaEstimada
from .views import totalGanaciaReal
from .views import DatosUsuario



#llamo a las view de las api 
from .views import UserViewSet
from .views import ProductViewSet
from .views import ProductOrderViewSet
from .views import AddressViewSet
from .views import CategoryViewSet
from .views import CustomerViewSet
from .views import OrderViewSet
from .views import ShopViewSet
from .views import EmailViewSet
from .views import PhoneViewSet





from rest_framework.routers import DefaultRouter
 
router =  DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'product', ProductViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'productorder', ProductOrderViewSet)
router.register(r'address', AddressViewSet)
router.register(r'order', OrderViewSet)
router.register(r'shop', ShopViewSet)
router.register(r'email', ShopViewSet)
router.register(r'phone', PhoneViewSet)








urlpatterns = router.urls

urlpatterns += [
    path('test/',csrf_exempt(TestView.as_view()),name="test" ),
    path('login/',csrf_exempt(UserView.as_view()),name="login" ),
    path('test_delete/<str:id>',csrf_exempt(TestView.as_view()), name="test" ), 
    path('createuser/',csrf_exempt(CrearCuenta.as_view()),name="createuser" ),  
    path('changepass/',csrf_exempt(ActualizarPassword.as_view()),name="changepass" ),  
    path('totaluser/',csrf_exempt(TotalUser.as_view()),name="totaluser" ),  
    path('ganancialestimada/',csrf_exempt(totalGanaciaEstimada.as_view()),name="ganancialestimada" ), 
    path('gananciareal/',csrf_exempt(totalGanaciaReal.as_view()),name="gananciareal" ),  
    path('datosuser/',csrf_exempt(DatosUsuario.as_view()),name="datosuser" ),  

]
