from django.urls import path
from .views import login, dashboard, verify, register_view

urlpatterns = [
    path('', register_view, name="register_view"),
    path('dashboard/', dashboard, name='dashboard'),
    path('verify/', verify, name='verify_view' ), 
 ]
