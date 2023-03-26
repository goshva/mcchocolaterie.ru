from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import Products

class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Products.get_products_by_id(ids)
        print(products)
        return render(request , 'cart.html' , {'products' : products} )

    def post(self, request):
        ids = list(request.session.get('cart').keys())
        products = Products.get_products_by_id(ids)
        remove = request.POST.get('remove')
        product = request.POST.get('product')
        cart = request.session.get('cart')
        inc = request.POST.get('inc')
        dec = request.POST.get('dec')

        if remove:
            print(product)
            cart.pop(product)
        
        if inc:
            cart[product] += 1
        
        if dec:
            if(cart[product] - 1) == 0:
               cart.pop(product)
            else: 
                cart[product] -= 1
        request.session['cart'] = cart
        return redirect('cart')

