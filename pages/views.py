from audioop import reverse
from base64 import urlsafe_b64decode, urlsafe_b64encode
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User

from checkout.models import Shipping
# Create your views here.
from products.models import Product, Category
from customer.models import Customer
from customer.forms import CustomerForm
from cart.models import *
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from firstpro.decorators import *
from django.contrib.auth.decorators import login_required

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_str, force_bytes 
# from django.utils import generate_token
from pages.tokens import account_activation_token
from django.core.mail import EmailMessage
from django.conf import settings
import threading


#ADDED this
class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()

#Added this to send email to user
def send_activation_email(user, request):
    current_site = get_current_site(request)
   
    email_subject = 'Activate your account'
    #add this html file
    email_body = render_to_string('authentication/activate.html', {
        'user': user,
        'domain': current_site,

        #Make pk attribute usable
        'uid': urlsafe_b64encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user)
    })

    email = EmailMessage(subject=email_subject, body=email_body,
                         from_email=settings.EMAIL_FROM_USER,
                         to=[user.email]
                         )

    if not settings.TESTING:
        EmailThread(email).start()


def login_view(request):
    users = User.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username)
        print(password)

        user = authenticate(request, username=username, password=password)
        #added this to add customers with username same as user
        customers=list( Customer.objects.filter(username=username))
        
        print("customers")
        print(customers)
        print("users")
        print(users)
        

        if user is not None:
            print("Reached here")
            
            #Check if customer exits and if the field is true
            if len(customers) ==1 and customers[0].user_email_verified:

                
            
                login(request, user)
            # print(user)
                return redirect('/')
            #if field is False send prompt to verify email
            elif not customers[0].user_email_verified:
                messages.add_message(request, messages.ERROR,
                                 'Email is not verified, please check your email inbox')
                context={'users':users}
                return render(request, 'login.html', context, status=401)

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
            # print("8888"+ customer_form )

            if pw == cpw:
                user = User.objects.create_user(un, em, pw)
                
                customer = customer_form.save(commit=False)
                customer.user = user
                
                #Send Email for verification to the user
                send_activation_email(request,user)
                user.save()
                customer.save()
                messages.success(request, 'Your account has been registered')
            elif pw != cpw:
                 messages.success(request, "Passwords don't match")

        
    context = {'customer_form': customer_form}

    return render(request, 'registration.html', context)

def activate_user(request, uidb64, token):

    try:
        uid = force_str(urlsafe_b64decode(uidb64))

        user = User.objects.get(pk=uid)

    except Exception as e:
        user = None

    if user and account_activation_token.check_token(user, token):
        #update customer field after verification
        customer = Customer.objects.get(username=user)
        customer.user_email_verified = True
        customer.save()
        user.save()

        messages.add_message(request, messages.SUCCESS,
                             'Email verified, you can now login')
        return redirect(reverse('login'))

    return render(request, 'authentication/activate-failed.html', {"user": user})

@login_required(login_url='login')
@admin_restricted
def admin_view(request):
    return render(request, "owner/admin.html")

@login_required(login_url='login')
@admin_restricted
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

def aboutus(request):
    return render(request, 'aboutus.html')

def helppage(request):
    return render(request, 'helppage.html')

