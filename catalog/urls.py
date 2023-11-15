from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
    path('', index,name='catalog_home'),
    path('category/<category_slug>', show_category,name='catalog_category'),
    path('product/(?p<product_slug>', show_product, name='catalog_product'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
