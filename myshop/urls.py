from django.contrib import admin
from django.urls import path, include
from AllPayments import urls as payments_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('custom_loggin.urls')),
    path('payments/', include(payments_urls)),
    path('products/', include('products.urls')),
]
