
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import MyUser
from .forms import RegisterForm, SignUpForm, UpdateUserForm, ChangePasswordForm, UserInfoForm
from . import kavesms
from .kavesms import get_random_otp
from django.contrib import messages
from payment.forms import ShippingForm
from payment.models import ShippingAddress
from django.contrib.auth.decorators import login_required

#user dashboard page 
@login_required
def dashboard(request):
    user = request.user
    form = UserInfoForm(instance=user)  # Pass the user instance to the form
    if request.method == 'POST':
        form = UserInfoForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            # Add success message or redirect to another page
    return render(request, 'custom_loggin/dashboard.html', {'user': user, 'form': form})

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
                messages.error(request, "زمان رمز یکبار مصرف به \ایان رسیده است دوباره امتحان کنید.")
                return HttpResponseRedirect(reverse('register_view'))

            if user.otp != int(request.POST.get('otp')):
                messages.error(request, "کد اشتباه وارد شد.")
                return HttpResponseRedirect(reverse('verify'))

            user.is_active = True
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('dashboard'))

        return render(request, 'custom_loggin/verify.html', {'mobile': mobile})

    except MyUser.DoesNotExist:
        messages.error(request, "خطا دوباره امتحان کنید.")
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
            messages.success(request, ("با موفقیت وارد شدید...خوش آمدید"))
            return redirect('product_list')
        else:
            messages.success(request, ("مشکلی پیش آمده...دوباره امتحان کنید"))
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

#adding user info after verify
def add_info(request):
      
	form = SignUpForm()
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			mobile = form.cleaned_data['mobile']
			password = form.cleaned_data['password1']
			# log in user
			user = authenticate(mobile=mobile, password=password)
			return redirect('update_info')
		else:
			messages.success(request, ("Whoops! There was a problem Registering, please try again..."))
			return redirect('register_view')
	else:
		return render(request, 'custom_loggin/add_info.html', {'form':form})

#update user 
def update_user(request):
	if request.user.is_authenticated:
		current_user = MyUser.objects.get(id=request.user.id)
		user_form = UpdateUserForm(request.POST or None, instance=current_user)

		if user_form.is_valid():
			user_form.save()

			login(request, current_user)
			messages.success(request, "اطلاعات حساب کاربری با موفقیت تغییر کرد!!")
			return redirect('dashboard')
		return render(request, "custom_loggin/update_user.html", {'user_form':user_form})
	else:
		messages.success(request, "لطفا ابتدا وارد شوید!!")
		return redirect('login')

#update user pass
def update_password(request):
	if request.user.is_authenticated:
		current_user = request.user
		if request.method  == 'POST':
			form = ChangePasswordForm(current_user, request.POST)

			if form.is_valid():
				form.save()
				messages.success(request, "پسورد شما با موفقیت تغییر یافت...")
				login(request, current_user)
				return redirect('update_user')
			else:
				for error in list(form.errors.values()):
					messages.error(request, error)
					return redirect('update_password')
		else:
			form = ChangePasswordForm(current_user)
			return render(request, "custom_loggin/update_password.html", {'form':form})
	else:
		messages.success(request, "لطفا ابتدا وارد شوید")
		return redirect('login')

#update user info
def update_info(request):
	if request.user.is_authenticated:
		# Get Current User
		current_user = MyUser.objects.get(user__id=request.user.id)
		# Get Current User's Shipping Info
		shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
		
		# Get original User Form
		form = UserInfoForm(request.POST or None, instance=current_user)
		# Get User's Shipping Form
		shipping_form = ShippingForm(request.POST or None, instance=shipping_user)		
		if form.is_valid() or shipping_form.is_valid():
			# Save original form
			form.save()
			# Save shipping form
			shipping_form.save()

			messages.success(request, "Your Info Has Been Updated!!")
			return redirect('product_list')
		return render(request, "custom_loggin/update_info.html", {'form':form, 'shipping_form':shipping_form})
	else:
		messages.success(request, "You Must Be Logged In To Access That Page!!")
		return redirect('product_list')
