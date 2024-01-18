from django.urls import path
from .views import product_list, add_product, product_detail

urlpatterns = [
    path('add/', add_product, name='add_product'),
    path('list/', product_list, name='product_list'),
    path('detail/<int:pk>/', product_detail, name='product_detail'),

    # path('secure/', secure_view, name='secure_page'),
]
