from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.db import connection
import datetime

from .models import Purchase
from .forms import PurchaseForm

# Create your views here.

def index(request,ProductID):
    with connection.cursor() as cursor:
        cursor.execute("""SELECT ProductName, ProductStock, ProductPrice 
                    FROM Product WHERE ProductID =%s""",[ProductID])
        Item = cursor.fetchall()
        cursor.close()
    if len(Item) == 0:
        raise Http404("The product does not exist.")
    elif int(Item[0][1]) < 1:
        raise Http404("The product is out of stock now!")

    if request.method == "POST":
        form = PurchaseForm(request.POST)
        if form.is_valid():
            with connection.cursor() as cursor:
                cursor.execute("""SELECT PurchaseID FROM Purchase 
                                WHERE PurchaseID = (SELECT MAX(PurchaseID) FROM Purchase)""")
                Max_id = cursor.fetchall()
                cursor.close()
            Purchase_ID = 1
            time_now = datetime.datetime.today().replace(microsecond=0)
            Total_price = int(request.POST['Amount']) * Item[0][2]

            if len(Max_id) != 0:
                Purchase_ID = Max_id[0][0] + 1
            with connection.cursor() as cursor:
                cursor.execute("INSERT Into Purchase values (%s,%s,%s,%s,%s,%s,%s,%s);",
                [Purchase_ID,ProductID,request.POST['USER_ID'],time_now,Total_price,request.POST['Requirement'],request.POST['Coupon_ID'],request.POST['Amount']])
                connection.commit()
                cursor.close()
            return HttpResponse("Your order has been processed! The Total price is %s!" % Total_price)
        else:
            return HttpResponse("That's not valid!")
    else:
        form = PurchaseForm()
        context = {'form':form, 'ProductName': Item[0][0],
                    'ProductPrice': Item[0][1],'ProductStock': Item[0][2]}
        return render(request, 'Purchase/Purchase.html',context)
