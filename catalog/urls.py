from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
    path('', index,name='catalog_home'),
    path('category/(?p<slug:category_slug>[-\w]+)', show_category, name='catalog_category'),
    path('product/(?p<slug:product_slug>[-\w]+)', show_product, name='catalog_product'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
