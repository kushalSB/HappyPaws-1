from django.shortcuts import render
from .forms import ProductForm
from .models import Product, Category
# Create your views here.
def create_products_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    object = Category.objects.all()
    context = {'form': form, 'object': object}
    return render(request, 'product/createproduct.html', context)

