from re import S
from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.contrib import admin
from customer.models import *
from products.models import *
# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    ordered_date = models.DateTimeField(auto_now_add=True)
    order_completed = models.BooleanField(default=False)
    order_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.customer)

    @property
    def getCartTotal(self):
        ordereditems = self.orderproduct_set.all()
        total = sum([item.getTotal for item in ordereditems])
        return total
    
    @property
    def getCartItems(self):
        ordereditems = self.orderproduct_set.all()
        total = sum([item.quantity for item in ordereditems])
        return total

    @property
    def shipping(self):
        shipping = False
        ordereditems = self.orderproduct_set.all()
        for i in ordereditems:
            shipping = True
        return shipping

        
        
class OrderProduct(models.Model):
    item = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ("Order no: " + str (self.id))
   
    @property
    def getTotal(self):
        total = self.item.price * self.quantity
        return total


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'ordered_date', 'order_id')
admin.site.register(Order, OrderAdmin)


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('item', 'order', 'quantity', 'date_added')
admin.site.register(OrderProduct, OrderProductAdmin)


    

    