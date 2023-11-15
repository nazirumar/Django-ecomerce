from django.shortcuts import render, get_object_or_404
from .models import Category, Product
# Create your views here.




def index(request):
    page_title = 'Music Instruments and Sheet Music for Musicians'
    return render(request, 'catalog/index.html', context={'page_title':page_title})


def show_category(request, category_slug):
    c = get_object_or_404(Category, category_slug)
    product = c.product_set.all()
    print(product)
    page_title = c.name
    meta_keywords = c.meta_keywords
    meta_description = c.meta_description
    context={
        'page_title':page_title,
        'meta_keywords':meta_keywords,
        'meta_descriptions':meta_description,
        'product':product,
        'c':c
    }
    return render(request, 'catalog/category.html',context)




def show_product(request, product_slug):
    p = get_object_or_404(Product, product_slug)
    categories = p.categories.filter(is_active=True)
    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description
    context = {
    'page_title': page_title,
    'meta_keywords': meta_keywords,
    'meta_descriptions': meta_description,
    'categories': categories,
    'p':p
    }

    return render(request, 'catalog/product.html', context)