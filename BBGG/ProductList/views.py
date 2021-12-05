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
        cursor.close()
        connection.close()
    if len(Item) == 0:
        raise Http404("The product does not exist.")
  
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            with connection.cursor() as cursor:
                cursor.execute("INSERT Into Cart values (%s,%s,%s,%s,%s);",
                [ProductID,request.POST['USER_ID'],request.POST['Amount'],Item[0][1],Item[0][3]])
                connection.commit()
                cursor.close()
                connection.close()
            return HttpResponse("This Item is now in your Cart!")
        else:
            return HttpResponse("That's not valid!")
    else:
        form = ProductForm()
        context = {'ProductID': Item[0][0], 'ProductName': Item[0][1],
                'ProductRegion': Item[0][2], 'ProductPrice': Item[0][3],
                'ProductDescription': Item[0][4], 'ProductCompany': Item[0][5],
                'ProductStock': Item[0][6], 'ProductDatecreated': Item[0][7],
                'ProductDatetour': Item[0][8],'form':form}
        return render(request, 'ProductList/detail.html',context)


    