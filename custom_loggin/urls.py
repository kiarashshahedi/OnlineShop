from django.urls import path
from .views import login, dashboard, verify, register_view

urlpatterns = [
    path('register', register_view, name="register"),
    path('dashboard/', dashboard, name='dashboard'),
    path('verify/', verify, name='verify' ), 
 ]
