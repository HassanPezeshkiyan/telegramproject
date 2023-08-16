from django.shortcuts import render
from .models import Product





def product_list(request):
    products = Product.objects.all()
    for item in products:
        print(item.image.url)
    return render(request, 'index.html', {'products': products})