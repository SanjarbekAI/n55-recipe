from django.urls import path

from shop.views import products_list_view

app_name = 'shop'

urlpatterns = [
    path('', products_list_view, name='products-list'),
]
