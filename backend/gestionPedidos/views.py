
from django.http import JsonResponse
from django.views import View
#import de los modelos
from .models import Product
#import para manejo de los pk
from django.forms.models import model_to_dict


#Lista con todos los productos desde la base
class ProductosListView(View):
    def get(self, request):
        productos = Product.objects.all()
        return JsonResponse(list(productos.values()), safe=False)
#lista con un producto especificado en la url por el pk
#validar cuando el pk no existe
class ProductoView(View):
    def get(self, request, pk):
        producto = Product.objects.get(pk=pk)
        return JsonResponse(model_to_dict(producto))



'''
def post(self, request):
        # post ...
    def put(self, request):
        # put...
    def delete(self, request):
        # delete...
'''