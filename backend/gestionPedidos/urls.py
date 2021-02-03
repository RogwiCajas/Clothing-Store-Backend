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

#llamo a las view de las api 
from .views import UserViewSet
from .views import ProductViewSet
from .views import ProductOrderViewSet
from .views import AddressViewSet
from .views import CategoryViewSet
from .views import CustomerViewSet
from .views import OrderViewSet
from .views import ShopViewSet


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





urlpatterns = router.urls

urlpatterns += [
    path('test/',TestView.as_view(),name="test" ),
    path('login/',csrf_exempt(UserView.as_view()),name="login" ),   
]