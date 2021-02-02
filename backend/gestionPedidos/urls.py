#Archivo creado para las urls de la api
from django.urls import path
from .views import ProductosListView, ProductoView
from .views import AddressListView, AddressView
from .views import CustomerListView, CustomerView
from .views import EmailListView, EmailView
from .views import OrderListView, OrderView
from .views import PhoneListView, PhoneView
from .views import ProductOrderListView, ProductOrderView
from .views import ShopListView, ShopView
from .views import UserListView, UserView



urlpatterns = [
    path('productos/', ProductosListView.as_view(), name="productos_list"),
    path('productos/<int:pk>/', ProductoView.as_view(), name="producto" ),
    path('address/', AddressListView.as_view(), name="address_list"),
    path('address/<int:pk>/', AddressView.as_view(), name="address" ),    
    path('customer/', CustomerListView.as_view(), name="customer_list"),    path('productos/<int:pk>/', ProductoView.as_view(), name="producto" ),
    path('customer<int:pk>/', CustomerView.as_view(), name="customer" ),    
    path('order/', OrderListView.as_view(), name="order_list"),    
    path('order/<int:pk>/', OrderView.as_view(), name="order" ),    
    path('productorder/', ProductOrderListView.as_view(), name="productorder_list"),
    path('productorder/<int:pk>/', ProductOrderView.as_view(), name="productorder" ),
    path('shop/', ShopListView.as_view(), name="shop_list"),
    path('shop/<int:pk>/', ShopView.as_view(), name="shop" ),
    path('user/', UserListView.as_view(), name="user_list"),
    path('user/<int:pk>/', UserView.as_view(), name="user" ),

]