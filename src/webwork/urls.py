"""webwork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from pages.views import home_view, contactpage, about_view, social_view
#from products.views import product_detial_view, product_create_view, dynamic_lookup_view
#from products.views import render dynamic_lookup_view
# from products.views import(
#     product_create_view,
#     product_detial_view,
#     render_initial_data,
#     dynamic_lookup_view,
#     product_list_view

# )
urlpatterns = [
    path('blog/', include('blog.urls')),
    path('courses/', include('courses.urls')),
    #path('products/<int:id>/', dynamic_lookup_view, name='product-detail'),
    # path('products/', product_list_view, name='product-list'),
    # path('products/<int:my_id>/', dynamic_lookup_view, name='product-detail'),
    # # path('', home_view, name='home'),
    # path('product/', product_detial_view, name='product-up'),
    # path('create/', product_create_view),
    # path('create/', render_initial_data),
    # path('contact/', contactpage),
    # path('about/', about_view),
    # path('social/', social_view),
    #path('products/<int:my_id>/', dynamic_lookup_view, name='product'),
    path('admin/', admin.site.urls),
]
