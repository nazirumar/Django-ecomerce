
## Django-ecomerce

# Ecomstore
    create views
       * 404_page

# Catalog App
    # create models
        Category Table
        Product Table
    # Views
        index
        show_category
        show_product

# djangoblog App
    # Create models
        Error Batch
        Error

# Utils App
    # Handle Context Variable for all the WebPages
        Create Context_processor.py File



# Templates
    # Create Templates Folder
    
        - base.html
        - index.html
        - category.html
        - product.html

        Subdir:
            catalog
                - category.html
                - index.html
                - product.html
            tags
                - category_list.html
                - navigation.html
            

# Static
    Css
        style.css
    Images
        products
            main
            thumbnail


# Shopping Cart App
    models
        - Our unique Cart ID value
        - Product ID
        - Date product was added to cart
        - Quantity in the cart

    Cart file
        function(
        - _cart_id
        - _generate_cart_id
        - get_cart_items
        - add_to_cart
        - cart_distinct_items)
        - show_cart
        - update_cart
        - delete cart
        - remove cart
        - cart_subtotal

        - # django template tags
            [^1 ] catalog_tags
            [^2 ] category_list

    FlatPage
        -- Settings
            - Install App
                'django.contrib.flatpages',

            - MIDDLEWARE_CLASSES
                'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
            ///  Add  SITE_ID  to your project settings
    Footer
        footer html file
        create tags           

            






    
        