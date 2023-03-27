from django.shortcuts import render, redirect
from django.core.mail import EmailMessage, get_connection
from django.conf import settings

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Products
from store.models.orders import Order

class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Products.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)
        listproducts = ""
        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price_5k,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            
            listproducts = listproducts +  product.name  +":"+  str(cart.get(str(product.id)))+ "\n"

            order.save()
        request.session['cart'] = {}


        with get_connection(  
            host=settings.EMAIL_HOST, 
            port=settings.EMAIL_PORT,  
            username=settings.EMAIL_HOST_USER, 
            password=settings.EMAIL_HOST_PASSWORD, 
            use_tls=settings.EMAIL_USE_TLS  
        ) as connection:
            subject = "Заказ" 
            email_from = settings.EMAIL_HOST_USER  
            recipient_list = ["mc_chocolaterie@mail.ru","mc.chocolate@yandex.ru","sha.egor@gmail.com"]  
            message = "Новый Заказ\n" + "Адресс: "+str(address) +"\n "+ "Телефон: "+ str(phone) +"\n "+listproducts
            EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()  
        return redirect('cart')


