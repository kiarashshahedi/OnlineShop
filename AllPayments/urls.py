from django.urls import path
from .views import process_payment, payment_success, payment_failure

urlpatterns = [
    path('process-payment/', process_payment, name='process_payment'),
    path('payment-success/', payment_success, name='payment_success'),
    path('payment-failure/', payment_failure, name='payment_failure'),
]
