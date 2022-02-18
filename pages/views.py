import imp
from multiprocessing import context
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
from django.contrib import messages


def login_view(request):
    users = User.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username)
        print(password)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
    context = {'users': users}
    return render(request, "login.html", context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def registration_view(request):
    customer_form = CustomerForm()

    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        
        if customer_form.is_valid():
            un = customer_form.cleaned_data['username']
            em = customer_form.cleaned_data['email']
            pw = customer_form.cleaned_data['password']
            cpw = request.POST.get('confirmpassword')
            

            if pw == cpw:
                user = User.objects.create_user(un, em, pw)
                user.save()
                customer = customer_form.save(commit=False)
                customer.user = user
                customer.save()
                messages.success(request, 'Your account has been registered')
            elif pw != cpw:
                 messages.success(request, "Passwords don't match")

        
    context = {'customer_form': customer_form}

    return render(request, 'registration.html', context)


def admin_view(request):
    return render(request, "owner/admin.html")

def admin_order_view(request):
    checkout = Shipping.objects.all()
    orders_customer = Order.objects.all()
    orders_products = OrderProduct.objects.all()
    context = {'checkout': checkout, 'orders_customer': orders_customer, 'orders_products': orders_products}
    return render(request, "owner/admin_orders.html", context)


def homepage_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        customer = request.user.customer
    # get or create order
        order, created = Order.objects.get_or_create(
            customer=customer, order_completed=False)
        items = order.orderproduct_set.all()
        cartItems = order.getCartItems
    else:
        items = []
        order = {'getCartTotal': 0, 'getCartItems': 0, 'shipping':False }
        cartItems = order['getCartItems']
    object = Category.objects.all()

   
    context = {'object': object,
               'items': items, 
               'cartItems': cartItems}
    return render(request, "homepage.html", context)




def searchProducts(request):
    if request.method=='GET':
        search = request.GET['search']
        products = Product.objects.filter(title__icontains=search)
    context = {'products': products}
    return render(request, 'search.html', context)

def update_discount_view(request):
    data = json.loads(request.body)
    orderId = data['orderId']
    action = data['action']
    order = Order.objects.get(id=orderId)
    customer = order.customer
    print(action, orderId)
    if action == 'add-discount' :
        if order.used_discount_points <3 and order.used_discount_points>=0:
             order.used_discount_points = (order.used_discount_points + 1)
             customer.reward_point = (customer.reward_point-1)

        
        
    elif action == 'remove-discount':
        if order.used_discount_points>0:
            order.used_discount_points = (order.used_discount_points - 1)
            customer.reward_point = (customer.reward_point+1)

       

    
    order.save()
    customer.save()

    return JsonResponse('Discount', safe=False)

def rootpage(request):
    category = Category.objects.all()

    context = {'category':category}
    return render(request, "rootpage.html", context)

def contact(request):
    return render(request, 'contactnew.html')

def grooming(request):
    return render(request, "services/grooming.html")

def pethostel(request):
    return render(request, "services/pethostel.html")

def vaccine(request):
    return render(request, "services/vaccine.html")


