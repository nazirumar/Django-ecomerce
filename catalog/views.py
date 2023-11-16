from django.shortcuts import render, get_object_or_404,redirect 
from .models import Category, Product
from .forms import ProductAddToCartForm
# Create your views here.
from cart import cart
from django.urls  import reverse
from django.http import HttpResponseRedirect



def index(request):
    page_title = 'Music Instruments and Sheet Music for Musicians'
    return render(request, 'catalog/index.html', context={'page_title':page_title})


def show_category(request, category_slug):
    c = get_object_or_404(Category, slug=category_slug)
    products = c.product_set.all()
    print(c)
    page_title = c.name
    meta_keywords = c.meta_keywords
    meta_description = c.meta_description
    context={
        'page_title':page_title,
        'meta_keywords':meta_keywords,
        'meta_descriptions':meta_description,
        'products':products,
        'c':c
    }
    return render(request, 'catalog/category.html',context)




def show_product(request, product_slug):
    p = get_object_or_404(Product, slug=product_slug)
    categories = p.categories.filter(is_active=True)
    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description
    # need to evaluate the HTTP method
    if request.method == 'POST':
        # add to cart__create th bound form
        postdata = request.POST.copy()
        form = ProductAddToCartForm(request, postdata)
        # check if posted data is valida
        if form.is_valid():
            # add to cart and redirct to cart page
            cart.add_to_cart(request)
            # if test cookie worked, get rid of it
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
            url = reverse('show_cart')
            return  redirect(url)
    else:
        # it's a GET,create the unbound form. Note request as  aKwargs
        form = ProductAddToCartForm(request=request, label_suffix=':')
        # assign the hidden input the product slug
    form.fields['product_slug'].widget.attrs['value'] = product_slug
    # set the test cookie on our first GET request
    request.session.set_test_cookie()
    print(form)
    context = {
    'page_title': page_title,
    'meta_keywords': meta_keywords,
    'meta_descriptions': meta_description,
    'categories': categories,
    'p':p,
    'form':form
    }


    return render(request, 'catalog/product.html', context)