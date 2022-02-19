<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
from django.shortcuts import redirect, render
from .models import Customer
# Create your views here.
from django.contrib.auth import  logout

def user_profile_view(request):
    return render(request, 'userprofile.html')


def deleteAccount(request, pk):
    customer = Customer.objects.get(id=pk)
    print(customer)
    if request.method == 'POST':
        password = request.POST.get('password')
        print(password)
        if password == customer.password:
            customer.user.delete()
            return redirect('/')
    return render(request, 'deleteAccount.html')


def baseuser(request):
    return render(request, 'base-user.html')

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
        

    return render(request, 'changePassword.html')

>>>>>>> frontend
