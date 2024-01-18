from django.urls import path
from . import views


urlpatterns = [
    path('', views.register_view, name='register_view'),
    path('verify/', views.verify, name='verify'),
    path('logout/', views.logout_view, name='logout_view'),
    path('dashboard/', views.dashboard, name='dashboard'),
]