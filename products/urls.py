from django.urls import path
from . import views
from custom_loggin import views as loggin_views





urlpatterns = [
    #adding product url
    path('add/', views.add_product, name='add_product'),

    #home page that shows all products
    path('', views.product_list, name='product_list'),

    #product details (after clicking on product list iteams views each iteam info)
    path('product_detail/<int:pk>/', views.product_detail, name='product_detail'),

    #user dashboard page (include user info - shopping info - & ...)
    path('dashboard/', loggin_views.dashboard, name='dashboard'),
    
    #website about page that shows seller info and ways for comunication
    #path('about/', views.about, name='about'),
    
    #category page
    path('category/<str:foo>', views.category, name='category'),

    #category summary
    path('category_summary/', views.category_summary, name="category_summary"),

    #search
    path('search/', views.search_view, name="search"),
    path('detail/<int:pk>/', views.detail_view, name='detail'),  # Define the detail view URL pattern

]