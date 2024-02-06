
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import MyUser
from .forms import RegisterForm, SignUpForm
from . import kavesms
from .kavesms import get_random_otp
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

#user dashboard page 
def dashboard(request):
    return render(request, "custom_loggin/dashboard.html")


#register user by sendding otp code from kavenegar
def register_view(request):
    form = RegisterForm

    if request.method == "POST":
        try:
            if "mobile" in request.POST:
                mobile = request.POST.get('mobile')
                user = MyUser.objects.get(mobile=mobile)
                # send otp
                otp = get_random_otp()
                # helper.send_otp(mobile, otp)
                kavesms.send_otp_soap(mobile, otp)
                print('OTP: ', otp)
                # save otp
                print(otp)
                user.otp = otp
                user.save()
                request.session['user_mobile'] = user.mobile
                return HttpResponseRedirect(reverse('verify'))

        except MyUser.DoesNotExist:
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                # send otp
                otp = get_random_otp()
                # helper.send_otp(mobile, otp)
                kavesms.send_otp_soap(mobile, otp)
                print('OTP: ', otp)
                # save otp
                print(otp)
                user.otp = otp
                user.is_active = False
                user.save()
                request.session['user_mobile'] = user.mobile
                return HttpResponseRedirect(reverse('verify'))
    return render(request, 'custom_loggin/register.html', {'form': form})

#check OTP for redirecting to dashboard or retry for loggin if inccorect
def verify(request):
    try:
        mobile = request.session.get('user_mobile')
        user = MyUser.objects.get(mobile = mobile)

        if request.method == "POST":

            # check otp expiration
            if not kavesms.check_otp_expiration(user.mobile):
                messages.error(request, "OTP is expired, please try again.")
                return HttpResponseRedirect(reverse('register_view'))

            if user.otp != int(request.POST.get('otp')):
                messages.error(request, "OTP is incorrect.")
                return HttpResponseRedirect(reverse('verify'))

            user.is_active = True
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('dashboard'))

        return render(request, 'custom_loggin/verify.html', {'mobile': mobile})

    except MyUser.DoesNotExist:
        messages.error(request, "Error accorded, try again.")
        return HttpResponseRedirect(reverse('register_view'))
    


#logout user(for all steps works)
def logout_view(request):
    logout(request)
    messages.success(request, (" شما خارج شدید"))
    return redirect('product_list')


#login user with mobile and password(superusers)
def login_user(request):
    if request.method == "POST":
        mobile = request.POST['mobile'] 
        password =  request.POST['password'] 
        user = authenticate(request, mobile=mobile, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("you have been logged in"))
            return redirect('product_list')
        else:
            messages.success(request, ("there is an error please try again"))
            return redirect('login')
    else:
        return render(request, 'custom_loggin/login.html', {})
        
#register user with mobile and password  
def UsernameRegister(request):
    form = SignUpForm
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            mobile = form.cleaned_data['mobile']
            password = form.cleaned_data['password1']
            #login user
            user = authenticate(mobile=mobile, password=password)
            login(request, user)
            messages.success(request, ("YOU have REGISTERed"))
            return redirect('product_list')
        else:
            messages.success(request, ("There was a problem in Register process"))
            return redirect('passRegister')
    else:
        return render(request, 'custom_loggin/passRegister.html', {'form':form})
    