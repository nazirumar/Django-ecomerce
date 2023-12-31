from django.shortcuts import render
from . import cart
# Create your views here.



def show_cart(request):
    if request.method == 'POST':
        postdata= request.POST.copy()
        if postdata['submit'] == 'remove':
            cart.remove_from_cart(request)
        if postdata['submit'] == 'Update':
            cart.update_cart(request)
    cart_items = cart.get_cart_items(request)
    page_title = 'Shopping Cart'
    cart_subtotal = cart.cart_subtotal(request)
    context={
        'page_title':page_title,
        'cart_items':cart_items,
        'cart_subtotal':cart_subtotal
    }
    return render(request, 'cart/cart.html', context)











