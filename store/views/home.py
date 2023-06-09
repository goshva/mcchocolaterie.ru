from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Products
from store.models.category import Category
from django.views import View


# Create your views here.
class Index(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        add = request.POST.get('add')
        fixed = request.POST.get('fixed')
        cart = request.session.get('cart')

        
        if cart:
            quantity = cart.get(product)
            if quantity:
                if fixed:
                    if remove:
                        if quantity<=1 or (quantity - int(fixed)) < 1:
                            cart.pop(product)
                        else:
                            cart[product] = quantity - int(fixed)
                    if add:
                            cart[product]  = quantity+int(fixed)
            else:
                cart[product] =int(fixed)
                #cart[product] = 1
        else:
            cart = {}
            cart[product] = int(fixed)
        request.session['cart'] = cart
        return redirect('homepage')



    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Products.get_all_products_by_categoryid(categoryID)
    else:
        products = Products.get_all_products();

    data = {}
    data['products'] = products
    data['categories'] = categories

    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)


