from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product, Category
from django.views.decorators.cache import cache_page
from .forms import ProductForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Product

#home page that shows list of products
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.select_related('category').all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    paginator = Paginator(products, 12)  # Show 12 products per page
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page.
        products = paginator.page(paginator.num_pages)

    return render(request, 'products/home-product-list.html', {'category': category, 'categories': categories, 'products': products})

#after clicking on a product on home page shows details of that product
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

#adding product on website(for admins)
@login_required(login_url='login')  # Require authentication to access this view
def add_product(request):
    # Check if the logged-in user is the superuser
    if not request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to add products.")

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            messages.success(request, 'Product added successfully!')
            return redirect('product_list')  # Redirect to the product list page
        else:
            messages.error(request, 'Error adding the product. Please check the form.')
    else:
        form = ProductForm()

    return render(request, 'products/add_product.html', {'form': form})

#about page of site and company owner
def about(request):
    return render(request, 'products/about.html')

#order the products in list of names called category page
def category(request, foo):
    #replacing Hyphens with space
    foo = foo.replace('-', ' ')
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'products/category.html', {'products':products, 'category':category})
    except:
        messages.success(request, 'This Category Doesnt Exist !')
        return redirect('product_list')

#summary of categories
def category_summary(request):
    categories = Category.objects.all()
    return render(request, 'category_summary.html', {"categories":categories})