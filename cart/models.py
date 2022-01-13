from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE

from customer.models import Customer
from products.models import Product
# Create your models here.





class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    ordered_date = models.DateTimeField(auto_now_add=True)
    order_completed = models.BooleanField(default=False)
    order_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

class OrderProduct(models.Model):
    item = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
   
   
    def __str__(self):
        return self.title
