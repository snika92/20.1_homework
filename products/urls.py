from django.urls import path

from products.apps import ProductsConfig
from products.views import ProductListView, contacts, MainView, ProductDetailView

app_name = ProductsConfig.name

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('contacts/', contacts, name='contacts'),
    path('products/', ProductListView.as_view(), name='index'),
    path('<int:pk>/products/', ProductDetailView.as_view(), name='about_product'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='about_product')
]