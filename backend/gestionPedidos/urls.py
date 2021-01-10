#Archivo creado para las urls de la api
from django.urls import path
from .views import ProductosListView, ProductoView

urlpatterns = [
    path('productos/', ProductosListView.as_view(), name="productos_list"),
    path('productos/<int:pk>/', ProductoView.as_view(), name="producto" ),
]