from django.urls import path
from .views import product_list, secure_view

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('secure/', secure_view, name='secure_page'),
]
