from ast import Pass
from django.shortcuts import render, redirect
from cart.models import *
from customer.forms import *
from products import *
from checkout import *
from products.forms import *
# Create your views here.


def delete_shipping_order(request, pk):
    order = OrderProduct.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/owner-orders/')
    context = {}
    return render(request, 'owner/delete_shipping.html', context)


def manageCustomer(request):
    customer = Customer.objects.all()
    context = {'customers': customer}
    return render(request, 'owner/manage_customer.html', context)


def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    user = request.user
    form = CustomerForm(request.POST)
    if request.method == 'POST':
        customer.name = request.POST.get('name')
        customer.email = request.POST.get('email')
        customer.phone = request.POST.get('phone')
        customer.reward_point = request.POST.get('reward_point')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if password != customer.password:
            if username != customer.username:
                user.username = username
                user.set_password(password)
                user.save()
                customer.password = password
                customer.username = username
        customer.save()
        return redirect('/manage-customer/')
    context = {'form': form, 'customer': customer}
    return render(request, 'owner/updateCustomer.html', context)


def deleteCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('/manage-customer/')
    context = {'customer': customer}
    return render(request, 'owner/deleteCustomer.html', context)


def manageProduct(request):
    product = Product.objects.all()
    context = {'products': product}
    return render(request, 'owner/manageProduct.html', context)


def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    category = Category.objects.all()
    form = ProductForm(request.POST, request.FILES)
    if request.method == 'POST':
        product.title = request.POST.get('title')
        product.price = request.POST.get('price')
        product.image = request.POST.get('image')
        product.description = request.POST.get('description')
        category_id = request.POST.get('category')
        category_object = Category.objects.get(id=category_id)
        product.category = category_object
        
        product.save()
        return redirect('/manage-product/')  

    context = {'form': form, 'product': product, 'category': category}
    return render (request,'owner/updateproduct.html', context )

def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        redirect('/manage-product/')
    context= {'product': product}
    return render(request, 'owner/deleteproduct.html', context)
