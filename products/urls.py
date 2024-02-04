from django.urls import path
from .views import product_list, add_product, product_detail, about
from custom_loggin import views




urlpatterns = [
    path('add/', add_product, name='add_product'),
    path('', product_list, name='product_list'),
    path('product_detail/<int:pk>/', product_detail, name='product_detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('about/', about, name='about'),

    
]