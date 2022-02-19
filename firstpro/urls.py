"""firstpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import thep include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from pages.views import (homepage_view,
                         contact_view,
                         login_view,
                         product_view,
                         cart_view,
                         admin_view,
                         checkout_view,
                         update_data_view,
                         registration_view,
                         processCheckout,
                         searchProducts
                         )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('register/', registration_view, name='register'),
    path('', homepage_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('product/<int:id>/', product_view, name='product'),
    path('cart/', cart_view, name='cart'),
    path('owner/', admin_view, name='owner'),
    path('checkout/', checkout_view, name='checkout'),
    path('update-cart/', update_data_view),
    path('process-checkout/', processCheckout, name='process-checkout'),
    path('search/', searchProducts, name= 'search')

]

# appending to the list
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
