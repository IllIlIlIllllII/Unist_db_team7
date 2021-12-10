from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

from .models import Product
from .forms import ProductForm, ProductForm2

#This is the ProductList page
def index(request):

    sort = request.GET.get('sort','')

    if sort == 'Price_ASC':
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM Product 
                            Order by ProductPrice Asc""")
            product_list = cursor.fetchall()
        context = {'Product_list': product_list}
        return render(request, 'ProductList/index.html',context)

    elif sort == 'Price_DESC':
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM Product 
                            Order by ProductPrice DESC""")
            product_list = cursor.fetchall()
        context = {'Product_list': product_list}
        return render(request, 'ProductList/index.html',context)

    elif sort == 'Company':
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM Product 
                            Order by ProductCompany ASC, ProductDateCreated Desc""")
            product_list = cursor.fetchall()
        context = {'Product_list': product_list}
        return render(request, 'ProductList/index.html',context)
        
    else:
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM Product 
                            Order by ProductDateCreated Desc""")
            product_list = cursor.fetchall()
        context = {'Product_list': product_list}
        return render(request, 'ProductList/index.html',context)

#This is the Product Detail page
def detail(request,ProductID):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Product WHERE ProductID =%s",[ProductID])
        Item = cursor.fetchall()

    if len(Item) == 0:
        raise Http404("The product does not exist.")
  
    if request.method == "POST":
        if request.session.get('User'):
            form = ProductForm2(request.POST)
        else:
            form = ProductForm(request.POST)
        if form.is_valid():
            if request.session.get('User'):
                user_id = request.session.get('User')
            else:
                user_id = request.POST['USER_ID']
            with connection.cursor() as cursor:
                cursor.execute("""SELECT ProductID, UserID FROM Cart 
                                WHERE ProductID = %s and UserID = %s""", [ProductID,user_id])
                check_vaild = cursor.fetchall()
            if len(check_vaild) != 0:
                with connection.cursor() as cursor:
                    cursor.execute("""UPDATE Cart SET Amount = %s
                                    WHERE ProductID = %s and UserID = %s """, [request.POST['Amount'],ProductID,user_id])
                    connection.commit()
                return HttpResponse("This Tour Item already in your Cart! <br><br>So, You changed the quantity of this Tour Items in your Cart.")
            with connection.cursor() as cursor:
                cursor.execute("""SELECT CartID FROM Cart 
                                WHERE CartID = (SELECT MAX(CartID) FROM Cart)""")
                Max_id = cursor.fetchall()
            Cart_ID = 1
            if len(Max_id) != 0:
                Cart_ID = Max_id[0][0] + 1
            with connection.cursor() as cursor:
                cursor.execute("INSERT Into Cart values (%s,%s,%s,%s,%s,%s);",
                [Cart_ID,ProductID,user_id,request.POST['Amount'],Item[0][1],Item[0][3]])
                connection.commit()
            return HttpResponse("This Tour Item is now in your Cart!")
        else:
            return HttpResponse("That's not valid!")
    else:
        if request.session.get('User'):
            form = ProductForm2()
        else:
            form = ProductForm()
        context = {'ProductID': Item[0][0], 'ProductName': Item[0][1],
                'ProductRegion': Item[0][2], 'ProductPrice': Item[0][3],
                'ProductDescription': Item[0][4], 'ProductCompany': Item[0][5],
                'ProductStock': Item[0][6], 'ProductDatecreated': Item[0][7],
                'ProductDatetour': Item[0][8],'form':form}
        return render(request, 'ProductList/detail.html',context)


    