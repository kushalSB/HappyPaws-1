import email
from email import message
import imp
from pyexpat.errors import messages
from re import search
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, response
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.messages import add_message, get_messages
from django.template import context
from checkout.models import Shipping
# Create your views here.
from products.models import Product
from customer.models import *
from customer.forms import CustomerForm, CreateUserForm
from cart.models import *
import json
from django.contrib.auth import authenticate, login, logout
import datetime

<<<<<<< HEAD
=======
from notification.models import Notification

>>>>>>> notice_backend

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username)
        print(password)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, "login.html")


def registration_view(request):
    customer_form = CustomerForm()

    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)

        if customer_form.is_valid():
            un = customer_form.cleaned_data['username']
            em = customer_form.cleaned_data['email']
            pw = customer_form.cleaned_data['password']

            user = User.objects.create_user(un, em, pw)

            user.save()

            customer = customer_form.save(commit=False)
            customer.user = user
            customer.save()

    context = {'customer_form': customer_form}

    return render(request, 'registration.html', context)


def admin_view(request):
    return render(request, "admin.html")


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

    products = Product.objects.all()
    context = {'products': products, 'items': items, 'cartItems': cartItems}
    return render(request, "homepage.html", context)


def contact_view(request, *args, **kwargs):

    context = {
        "new": "old",
        "num": 123
    }
    return render(request, "contact.html", context)

# class ItemDetailView(DetailView):
#   model = Item
#     # context = {
#     #     'items': Item.objects.all()
#     # }
#     # return render(request, "items.html", context)
#   template_name = "detail.html"


def product_view(request, id):
    if request.user.is_authenticated:
        customer = request.user.customer
    # get or create order
        order, created = Order.objects.get_or_create(
            customer=customer, order_completed=False)
        items = order.orderproduct_set.all()
        cartItems = order.getCartItems
    else:
        items = []
        order = {'getCartTotal': 0, 'getCartItems': 0}
        cartItems = order['getCartItems']
    object = Product.objects.get(id=id)
    context = {'object': object, 'cartItems': cartItems,'shipping':False}
    return render(request, "product/detail.html", context)


def cart_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, order_completed=False)
        items = order.orderproduct_set.all()
    else:
        items = []
        order = {'getCartTotal': 0, 'getCartItems': 0,'shipping':False}

    context = {'items': items, 'order': order}
    return render(request, "cart.html", context)


def checkout_view(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        # get or create order
        order, created = Order.objects.get_or_create(
            customer=customer, order_completed=False)
        items = order.orderproduct_set.all()
        cartItems = order.getCartItems
    else:
        items = []
        order = {'getCartTotal': 0, 'getCartItems': 0}
        cartItems = order['getCartItems']

    context = {'items': items, 'order': order, 'cartItems': cartItems, 'shipping':False}
    return render(request, 'checkout.html', context)


def update_data_view(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print(action, productId)

    customer = request.user.customer
    item = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, order_completed=False)
    orderProduct, created = OrderProduct.objects.get_or_create(
        order=order, item=item)

    if action == 'add':
        orderProduct.quantity = (orderProduct.quantity + 1)
    elif action == 'remove':
        orderProduct.quantity = (orderProduct.quantity - 1)

    orderProduct.save()

    if orderProduct.quantity <= 0:
        orderProduct.delete()

    return JsonResponse('Item added to cart', safe=False)


def processCheckout(request):
    print(request.body)
    transactionId = datetime.datetime.now().timestamp()
    checkoutData = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, order_completed=False)
        cart_total= float(checkoutData['form']['cart_total'])
        order.order_id = transactionId

        if cart_total == order.getCartTotal:
            order.order_completed = True
        order.save()

        if order.shipping == True:
            Shipping.objects.create(
                customer= customer,
                order = order,
                city = checkoutData['shipping']['city'],
                address = checkoutData['shipping']['address'],
            )
    else:
        print('no user')
    return JsonResponse('Order placed', safe=False)

def searchProducts(request):
    search = request.GET['search']
    products = Product.objects.filter(title__icontains=search)
    context = {'products': products}


<<<<<<< HEAD
    return render(request, 'search.html', context)
=======
    return render(request, 'search.html', context)

def notification_view(request):
    notifications = Notification.objects.all
    context = {'notice':notifications}
    return render(request, "notifications.html", context)

def notification_delete(request,pk):

    notifications = Notification.objects.get(id=pk)

    if request.method == 'POST':
        notifications.delete()
        return redirect('home')
        
    context = {'object': notifications}
    return render(request, "delete_template.html", context)
>>>>>>> notice_backend
