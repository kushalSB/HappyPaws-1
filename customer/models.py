from re import T
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib import admin


# Create your models here.

class Customer(models.Model):
<<<<<<< HEAD
=======
    id = models.AutoField(auto_created=True, primary_key=True)
>>>>>>> frontend
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=10, null=True)
    username = models.CharField(max_length=300, null=True, blank=True)
    password = models.CharField(max_length=300, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
<<<<<<< HEAD
=======
    reward_point = models.FloatField(default = 0, null=True, blank=True)
>>>>>>> frontend


    def __str__(self):
        return self.name 
<<<<<<< HEAD



class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone','username', 'password', 'date_created')
=======
    
    @property
    def getVouchers(self):
        total = self.reward_point
        return total


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone','username', 'password', 'date_created', 'reward_point', 'user')
>>>>>>> frontend
admin.site.register(Customer, CustomerAdmin)
    
    

