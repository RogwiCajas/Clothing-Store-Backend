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
from .views import totalGanacia
from .views import OrdenesPorFecha



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
<<<<<<< HEAD
    path('test/',TestView.as_view(),name="test" ),
    path('login/',csrf_exempt(UserView.as_view()),name="login" ), 
    path('createuser/',csrf_exempt(CrearCuenta.as_view()),name="changePass" ),  
    path('changePass/',csrf_exempt(ActualizarPassword.as_view()),name="changePass" ),  
    path('totaluser/',csrf_exempt(TotalUser.as_view()),name="changePass" ),  
    path('totalganancia/',csrf_exempt(totalGanacia.as_view()),name="changePass" ),  
    path('ordenfecha/',csrf_exempt(OrdenesPorFecha.as_view()),name="changePass" ),  
]


=======
    path('test/',csrf_exempt(TestView.as_view()),name="test" ),
    path('login/',csrf_exempt(UserView.as_view()),name="login" ),
    path('test_delete/<str:id>',csrf_exempt(TestView.as_view()), name="test" ),   
]
>>>>>>> 53dd3a1bf42fd3e9fa02bf102b92dbf4fc8a5bd4
