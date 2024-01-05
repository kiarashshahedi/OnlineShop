# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate, login, logout
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .forms import CustomUserCreationForm


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
