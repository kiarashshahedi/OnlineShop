from django.shortcuts import render
from django.http import HttpResponseRedirect
from payments import get_payment_model

def process_payment(request):
    payment = get_payment_model().objects.create(
        variant="default",
        description="Payment for your product or service",
        total="10.00",  # Replace with the actual amount
        currency="USD",
    )

    return HttpResponseRedirect(payment.get_process_url())

def payment_success(request):
    return render(request, 'payment_success.html')

def payment_failure(request):
    return render(request, 'payment_failure.html')
