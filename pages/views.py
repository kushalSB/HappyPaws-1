from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from products.models import Product

def login_view(request):
  return render(request,"login.html")

def admin_view(request):
  return render(request,"admin.html")



def homepage_view(request, *args, **kwargs):
    products = Product.objects.all()
    context = {'products': products}
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

def product_view(request, *args, **kwargs):
    context = {}
    return render(request, "product/detail.html", context)

def cart_view(request, *args, **kwargs):
  context={}
  return render(request, "cart.html")


