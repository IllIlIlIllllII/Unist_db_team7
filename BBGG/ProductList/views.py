from django.shortcuts import render
from django.http import HttpResponse

from .models import Product
# Create your views here.

def index(request):
    latest_product_list = Product.objects.order_by('-ProductDateCreated')
    context = {'latest_Product_list': latest_product_list}
    return render(request, 'ProductList/index.html',context)
    