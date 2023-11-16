from django.shortcuts import render
from . import cart
# Create your views here.



def show_cart(request):
    cart_item_count = cart.cart_item_count(request)
    page_title = 'Shopping Cart'
    context={
        'page_title':page_title,
        'cart_item_count':cart_item_count
    }
    return render(request, 'cart/cart.html', context)











