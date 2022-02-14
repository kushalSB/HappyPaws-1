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
                         logoutUser,
                         product_view,
                         cart_view,
                         admin_view,
                         admin_order_view,
                         checkout_view,
                         update_data_view,
                         registration_view,
                         processCheckout,
                         searchProducts,
                         update_discount_view,
                         product_category_view,
                         rootpage,
                         contact
                         )
from products.views import(
    create_products_view,
   
)

from customer.views import(
    user_profile_view,
    deleteAccount,
    changePassword,
    baseuser,

)
from owner.views import (
    delete_shipping_order,
    deleteCustomer,
    manageCustomer,
    updateCustomer,
    manageProduct,
    deleteProduct,
    updateProduct,
    


)
    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('register/', registration_view, name='register'),
    path('', homepage_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('product/<int:id>/', product_view, name='product'),
    path('product-by-category/<str:choice>/', product_category_view, name= 'product-by-category' ),
    path('cart/', cart_view, name='cart'),

    path('owner/', admin_view, name='owner'),
    path('owner-orders/', admin_order_view, name='owner-orders'),
    path('owner/delete-orders/<int:pk>', delete_shipping_order, name='delete-orders'),
    path('manage-customer/', manageCustomer, name='manage-customer'),
    path('update-customer/<int:pk>/', updateCustomer, name='update-customer'), 
    path('delete-customer/<int:pk>/', deleteCustomer, name='delete-customer'),
    path('manage-product/', manageProduct, name='manage-product'),
    path('update-product/<int:pk>/', updateProduct, name='update-product'), 
    path('delete-product/<int:pk>/', deleteProduct, name='delete-product'),

    path('checkout/', checkout_view, name='checkout'),
    path('update-cart/', update_data_view),
    path('process-checkout/', processCheckout, name='process-checkout'),
    path('search/', searchProducts, name= 'search'),

    path('create-product', create_products_view, name='create-product'),
    


    path('logout/', logoutUser, name='logout'),
    path('update-discount/', update_discount_view),
    path('root/', rootpage), 
    path('contact/',contact ),
    path('user-profile/', user_profile_view,name='user-profile'),
    path('delete-account/<int:pk>/', deleteAccount, name='delete-account'),
    path('change-password/<int:pk>/', changePassword, name='change-password'),
    path('baseuser', baseuser),
    

]

# appending to the list
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
