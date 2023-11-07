from django.urls import path

from products.apps import ProductsConfig
from products.views import index, contacts, main, about_product

app_name = ProductsConfig.name

urlpatterns = [
    path('', main, name='main'),
    path('contacts/', contacts, name='contacts'),
    path('index/', index, name='index'),
    path('<int:pk>/products/', about_product, name='about_product')
]