from django.urls import path
from .views import *

urlpatterns =[
    path('', index,name='catalog_home'),
    path('category/(?<category_slug>[-\w]+)/$', show_category,name='catalog_category'),
    path('product/(?p<product_slug>[-\w]/$)', show_product, name='catalog_product'),

]