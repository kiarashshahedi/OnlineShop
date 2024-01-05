from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product, Category
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page

@login_required
def secure_view(request):
    return render(request, 'products/secure_page.html', {'user': request.user})

@cache_page(60 * 15)  # Cache for 15 minutes
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

    return render(request, 'products/product_list.html', {'category': category, 'categories': categories, 'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    return render(request, 'products/product_detail.html', {'product': product})
#-----------------------------------------------------------------------------
