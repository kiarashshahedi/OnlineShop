from django.contrib import admin
from django.urls import path, include
from payments import urls as payments_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('products.urls')),
    path('payments/', include(payments_urls)),
]
