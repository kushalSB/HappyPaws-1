from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, response
from django.contrib import auth
from django.contrib.auth.models import User
from checkout.models import Shipping
# Create your views here.
from products.models import Product, Category
from customer.models import *
from customer.forms import CustomerForm, CreateUserForm
from cart.models import *
import json
from django.contrib.auth import authenticate, login, logout
import datetime

def user_profile_view(request):
    return render(request, 'customer/userprofile.html')


def deleteAccount(request, pk):
    customer = Customer.objects.get(id=pk)
    print(customer)
    if request.method == 'POST':
        password = request.POST.get('password')
        print(password)
        if password == customer.password:
            customer.user.delete()
            return redirect('/')
    return render(request, 'customer/deleteAccount.html')


def baseuser(request):
    return render(request, 'customer/base-user.html')

def changePassword(request, pk):
    customer = Customer.objects.get(id=pk)
    user = request.user
    print(customer)
    if request.method == 'POST':
        password = request.POST.get('old-password')
        new_password = request.POST.get('new-password')
        confirm_passowrd = request.POST.get('confirm-password')
        if password == customer.password:
            if new_password == confirm_passowrd:
                customer.password = new_password
                customer.save()
                user.set_password(new_password)
                user.save()

        print(password)
        

    return render(request, 'customer/changePassword.html')

