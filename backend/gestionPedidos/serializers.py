from rest_framework import serializers
from .models import User
from .models import Product
from .models import ProductOrder
from .models import Phone
from .models import Address
from .models import Category
from .models import Customer
from .models import Email
from .models import Shop
from .models import Order
from .models import User
#cambios

class UserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProductSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

        
class ProductOrderSerilizer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = '__all__'
    
class PhoneSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'

class AddressSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class CategorySerilizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CustomerSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class EmailSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'

class ShopSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'
           
class OrderSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
    
