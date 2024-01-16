from django.urls import path
from .views import product_list

urlpatterns = [
    path('productList', product_list, name='product_list'),
    # path('secure/', secure_view, name='secure_page'),
]
