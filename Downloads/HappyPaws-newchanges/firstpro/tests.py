from ast import arg
import imp
from turtle import home
from venv import create
from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from customer.views import *
from cart.views import *
from products.views import *
from checkout.views import *
from owner.views import *
from pages.views import *



class TestUrls(SimpleTestCase):
    
    def test_login_view(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login_view)

    def test_registration_view(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, registration_view)

    def test_update_customer(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, homepage_view)

    def test_contact(self):
        url = reverse('contact')
        self.assertEquals(resolve(url).func, contact)

    def test_productbycategory(self):
        url = reverse('product-by-category', args=[1])
        self.assertEquals(resolve(url).func, product_category_view)

    def test_product(self):
        url = reverse('product', args=[1])
        self.assertEquals(resolve(url).func, product_view)

    def test_owner(self):
        url = reverse('owner')
        self.assertEquals(resolve(url).func,  admin_view)

    def test_owner_orders(self):
        url = reverse('owner-orders')
        self.assertEquals(resolve(url).func, admin_order_view)

    def test_delete_orders(self):
        url = reverse('delete-orders', args=[1])
        self.assertEquals(resolve(url).func,  delete_shipping_order)

    def test_manage_customer(self):
        url = reverse('manage-customer')
        self.assertEquals(resolve(url).func, manageCustomer)

    def test_update_customers(self):
        
        url = reverse('update-customer', args=[1])
        self.assertEquals(resolve(url).func, updateCustomer)

    def test_delete_customers(self):
        url = reverse('delete-customer', args=[1])
        self.assertEquals(resolve(url).func, deleteCustomer)

    def test_manage_product(self):
        url = reverse('manage-product')
        self.assertEquals(resolve(url).func, manageProduct)

    def test_update_product(self):
        
        url = reverse('update-product', args=[1])
        self.assertEquals(resolve(url).func, updateProduct)

    def test_delete_product(self):
        
        url = reverse('delete-product', args=[1])
        self.assertEquals(resolve(url).func, deleteProduct)

    def test_checkout(self):
        url = reverse('checkout')
        self.assertEquals(resolve(url).func, checkout_view)

    def test_update_cart(self):
        url = reverse('update-cart')
        self.assertEquals(resolve(url).func, update_data_view)

    def test_proceses_checkout(self):
        url = reverse('process-checkout')
        self.assertEquals(resolve(url).func, processCheckout)

    def test_search(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func, searchProducts)

    def test_create_product(self):
        url = reverse('create-product')
        self.assertEquals(resolve(url).func, create_products_view)

    def test_logout(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logoutUser)

    def test_update_discount(self):
        url = reverse('update-discount')
        self.assertEquals(resolve(url).func,  update_discount_view)

    def test_rootpage(self):
        url = reverse('rootpage')
        self.assertEquals(resolve(url).func,  rootpage)

    def test_user_profile(self):
        url = reverse('user-profile')
        self.assertEquals(resolve(url).func, user_profile_view)

    def test_delete_account(self):
        url = reverse('delete-account', args=[1])
        self.assertEquals(resolve(url).func, deleteAccount)

    def test_change_password(self):
        url = reverse('change-password',args= [1])
        self.assertEquals(resolve(url).func, changePassword)
