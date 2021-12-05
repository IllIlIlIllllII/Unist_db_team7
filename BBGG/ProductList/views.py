from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

from .models import Product
from .forms import ProductForm
# Create your views here.

def index(request):
    latest_product_list = Product.objects.order_by('-ProductDateCreated')
    context = {'latest_Product_list': latest_product_list}
    return render(request, 'ProductList/index.html',context)

def detail(request,ProductID):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Product WHERE ProductID =%s",[ProductID])
        Item = cursor.fetchall()
    if len(Item) == 0:
        raise Http404("The product does not exist.")
    context = {'ProductID': Item[0][0], 'ProductName': Item[0][1],
                'ProductRegion': Item[0][2], 'ProductPrice': Item[0][3],
                'ProductDescription': Item[0][4], 'ProductCompany': Item[0][5],
                'ProductStock': Item[0][6], 'ProductDatecreated': Item[0][7],
                'ProductDatetour': Item[0][8]}
    return render(request, 'ProductList/detail.html',context)


    