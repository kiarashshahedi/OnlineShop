from django.contrib import admin
from django.urls import path, include
from AllPayments import urls as payments_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('custom_loggin.urls')),
    #path('home/', include('home.urls')),
    path('payments/', include(payments_urls)),
    path('', include('products.urls')),
]
