from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug =models.SlugField(max_length=100,unique=True,help_text="Unique valuefor product Page url, created from name.")
    description =models.TextField()
    is_active = models.BooleanField(default=True)
    meta_keywords = models.CharField("Meta Keywords",max_length=255,help_text="Comman-delimited set of SEO Keywods for meta tag")
    meta_description = models.CharField("Meta Descriptions", max_length=255,help_text='Content for description meta tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'categories'
        ordering = ['-created_at']
        verbose_name_plural = 'Categories'


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return ('catalog_category', (), { 'category_slug': self.slug })
    


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, help_text='Unique value for product page URL, created from name.')
    sku = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    old_price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, default=0.00)
    image = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    quantity = models.IntegerField()
    description = models.TextField()
    meta_keywords = models.CharField(max_length=255, help_text='Comman-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField(max_length=255,help_text='Content for description meta tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)


    class Meta:
        db_table = 'products'
        ordering = ['-created_at']

    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        return ('catalog_product', (), { 'product_slug': self.slug })
    
    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None