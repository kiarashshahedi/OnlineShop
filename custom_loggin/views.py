
from .forms import *
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import MyUser
from . import kavesms
from django.shortcuts import render, redirect


#--------------------------------------------------------------------------------------------
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate, login, logout
# from django.shortcuts import render, redirect
# from django.contrib import messages

# def signup(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, 'Registration successful. You are now logged in.')
#             return redirect('products/product_list')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'accounts/signup.html', {'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, 'Login successful.')
#             return redirect('products/product_list')
#         else:
#             messages.error(request, 'Invalid username or password.')
#     return render(request, 'accounts/login.html')

# @login_required
# def logout_view(request):
#     logout(request)
#     messages.success(request, 'Logout successful.')
#     return redirect('products/product_list')
#----------------------------------------------------------------------------------------------
def login(request):
    if request.method == "POST":
        if "mobile" in request.POST:
            mobile = request.POST.get(mobile)
            user = MyUser.objects.get(mobile = mobile)
            login(request, user)
            return HttpResponseRedirect(reverse('dashboard'))
    return render(request, 'custom_loggin/register.html')
#------------------------------------------------------------------------
def dashboard(request):
    return render(request, "custom_loggin/dashboard.html")

def register_view(request):

    form = RegisterForm

    if request.method == "POST":
        try:
            if "mobile" in request.POST:
                mobile = request.POST.get('mobile')
                user = MyUser.objects.get(mobile=mobile)
                #send otp
                otp = kavesms.get_random_otp()
                # kavesms.send_otp(mobile, otp)
                #kavesms.send_otp_soap(mobile, otp)
                #save otp
                print(otp)
                user.otp = otp
                user.save()
                #showing user phone number 
                request.session['user_mobile'] = user.mobile
                #redirect to page
                return HttpResponseRedirect(reverse('verify'))
        except MyUser.DoesNotExist:
            form = forms.RegisterForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                #send otp
                otp = kavesms.get_random_otp()
                # kavesms.send_otp(mobile, otp)
                #kavesms.send_otp_soap(mobile, otp)
                #save otp
                print(otp)

                user.otp = otp
                user.is_active = False
                user.save()
                #showing user phone number 
                request.session['user_mobile'] = user.mobile
                #redirecting to verify page
                return redirect(reverse('verify'))
    return render(request, "custom_loggin/register.html", {'form': form})


#check OTP for redirecting to dashboard or retry for loggin if inccorect

def verify(request):
    try:
        mobile = request.session.get('user_mobile')
        user = MyUser.objects.get(mobile=mobile)

        if request.method == 'POST':

            entered_otp = int(request.POST.get('otp'))
            if user.otp != entered_otp:

                print(f"Incorrect OTP entered: {entered_otp}")
                return redirect(reverse("register_view"))
            
            user.is_active = True
            user.save()
            login(request, user)
            return redirect(reverse("dashboard"))

        return render(request, 'custom_loggin/verify.html', {'mobile': mobile})
    
    except:
        print(f"User with mobile {mobile} does not exist.")
        return redirect(reverse("register_view"))
    
    # except Exception as e:
    #     # Handle other exceptions if necessary
    #     print(f"An error occurred during OTP verification: {e}")
    #     return redirect(reverse("register_view"))