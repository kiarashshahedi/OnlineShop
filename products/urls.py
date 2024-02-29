from django.urls import path
from .views import product_list, add_product, product_detail, about, category
from custom_loggin import views




urlpatterns = [
    #adding product url
    path('add/', add_product, name='add_product'),

    #home page that shows all products
    path('', product_list, name='product_list'),

    #product details (after clicking on product list iteams views each iteam info)
    path('product_detail/<int:pk>/', product_detail, name='product_detail'),

    #user dashboard page (include user info - shopping info - & ...)
    path('dashboard/', views.dashboard, name='dashboard'),
    
    #website about page that shows seller info and ways for comunication
    path('about/', about, name='about'),
    
    #category page
    path('category/<str:foo>', category, name='category'),

]