from re import T
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib import admin


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=10, null=True)
    username = models.CharField(max_length=300, null=True, blank=True)
    password = models.CharField(max_length=300, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.name 



class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone','username', 'password', 'date_created')
admin.site.register(Customer, CustomerAdmin)
    
    

