from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    product_list = Product.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(product_list, 5)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    
    context = {
        'products' : products
    }
    return render(request, './home.html', context)
