from django import template

register = template.Library ()


@register.filter (name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys ()
    for id in keys:
        if int (id) == product.id:
            return True
    return False;


@register.filter (name='cart_quantity')
def cart_quantity(product, cart):
    keys = cart.keys ()
    for id in keys:
        if int (id) == product.id:
            return cart.get (id)
    return 0;

@register.filter (name='cart_total')
def cart_total(products, cart):
    total = 0
    for p in products:
        total += cart_quantity(p, cart)
    return total


@register.filter (name='price_total')
def price_total(product, cart):
    return product.price_5k * cart_quantity (product, cart)  #make price switch by sum over 5000, 10000, 15000, 20000 (discount from quantity * price)

@register.filter (name='10k_discount')
def disc_10k(product, cart):
    return product.price_10k * cart_quantity (product, cart)

@register.filter (name='20k_discount')
def disc_20k(product, cart):
    return product.price_20k * cart_quantity (product, cart)

@register.filter (name='many_discount')
def disc_many(product, cart):
    return product.price_many * cart_quantity (product, cart)

@register.filter (name='total_cart_price')
def total_cart_price(products, cart):
    sum = 0
    for p in products:
            sum += price_total (p, cart)
    print(sum)
    if sum >= 20000:
        sum = 0
        for p in products:
            sum += disc_many (p, cart)
        return sum
    elif sum >= 10000:
        sum = 0
        for p in products:
            sum += disc_20k (p, cart)
        return sum 
    elif sum >= 5000:
        sum = 0
        for p in products:
            sum += disc_10k (p, cart)
        return sum    
    else: 
        return sum
     
    

