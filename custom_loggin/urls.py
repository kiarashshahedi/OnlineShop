from django.urls import path
from . import views


urlpatterns = [

    #Register with Mobile and OTP
    path('register/', views.register_view, name='register_view'),
    #verify OTP code TRUE or FALSE 
    path('verify/', views.verify, name='verify'),

    #User dashboard page
    path('dashboard/', views.dashboard, name='dashboard'),

    #logout(for all parts used)
    path('logout/', views.logout_view, name='logout_view'), 

    #Login with Mobile and password
    path('login/', views.login_user, name='login'),

    #Register with Mobile and Password
    path ('passRegister/', views.UsernameRegister, name='passRegister')


]