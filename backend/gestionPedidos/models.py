from django.db import models
from mongoengine import DynamicDocument, fields, Document

# Create your models here.

class User(models.Model):
    user_id = models.CharField(max_length=10, primary_key=True)
    user_password= models.CharField(max_length=20)

    def __str__(self):
        return (self.user_id) 

class Address(models.Model):
    address_id = models.CharField(max_length=10, primary_key=True)
    address_country= models.CharField(max_length=20)
    address_province= models.CharField(max_length=20)
    address_city= models.CharField(max_length=30)   
    address_zone= models.CharField(max_length=30)
    address_neighnorhood= models.CharField(max_length=30)   
    address_street= models.CharField(max_length=50)   
    address_buildingNo= models.IntegerField()   

    def __str__(self):
        return self.address_id
 

class Customer(models.Model):
    customer_id = models.CharField(max_length=10, primary_key=True)
    customer_FirstName= models.CharField(max_length=40)
    customer_LastName= models.CharField(max_length=40)
    customer_address= models.ForeignKey(Address,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return (self.customer_id) 

class Email(models.Model):
    email = models.EmailField(max_length=60, primary_key=True)
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
   
    def __str__(self):
        return (self.email) 

class Phone(models.Model):
    phone = models.CharField(max_length=10, primary_key=True)
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    phone_provider= models.CharField(max_length=20)

    def __str__(self):
        return (self.phone) 


class Shop(models.Model):
    shop_id = models.CharField(max_length=10, primary_key=True)
    address_id = models.ForeignKey(Address,on_delete=models.CASCADE)
    shop_name= models.CharField(max_length=60)
    shop_description= models.CharField(max_length=200)

    def __str__(self):
        return (self.shop_id)  

class Order(models.Model):
    order_id = models.CharField(max_length=10, primary_key=True)
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    address_id = models.ForeignKey(Address,on_delete=models.CASCADE)
    shop_id = models.ForeignKey(Shop,on_delete=models.CASCADE)
    order_date= models.DateTimeField()
    order_amount= models.FloatField()
    order_descount= models.FloatField()

    def __str__(self):
        return (self.order_id)   

class Category(models.Model):
    category_id = models.CharField(max_length=10, primary_key=True)
    category_name= models.CharField(max_length=40)
    category_description= models.CharField(max_length=200)

    def __str__(self):
        return (self.category_id)   
    
class Product(models.Model):
    product_id = models.CharField(max_length=10, primary_key=True)
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_name= models.CharField(max_length=20)
    product_description= models.CharField(max_length=20)
    product_price= models.FloatField()
    product_descount= models.FloatField()
    product_stock= models.IntegerField()
    product_isOffer= models.BooleanField()
    product_isHighlighted= models.BooleanField(default=False)
    product_gender= models.CharField(max_length=1) #m , f
    product_color= models.CharField(max_length=20)
    product_size= models.CharField(max_length=5)



    def __str__(self):
        return (self.product_id)   

class ProductOrder(models.Model):
    productOrder_id = models.CharField(max_length=10, primary_key=True)
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    productOrder_subtotal= models.FloatField()
    productOrder_discount= models.FloatField()
    productOrder_total= models.FloatField()

    def __str__(self):
        return (self.productOrder_id)  

class Test(Document):
    meta = {'collection' : 'test'}
    nombre = fields.StringField()

    #def __str__(self):
    #    return (self.nombre) 