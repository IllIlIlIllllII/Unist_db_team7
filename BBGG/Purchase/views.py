from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.db import connection
import datetime

from .models import Purchase
from .forms import PurchaseForm, PurchaseForm2

# Create your views here.

def index(request,ProductID):
    with connection.cursor() as cursor:
        cursor.execute("""SELECT ProductName, ProductStock, ProductPrice 
                    FROM Product WHERE ProductID =%s""",[ProductID])
        Item = cursor.fetchall()
    if len(Item) == 0:
        raise Http404("The product does not exist.")
    elif int(Item[0][1]) < 1:
        raise Http404("The product is out of stock now!")

    if request.method == "POST":
        if request.session.get('User'):
            form = PurchaseForm2(request.POST)
        else:
            form = PurchaseForm(request.POST)
        if form.is_valid():
            
            if request.session.get('User'):
                user_id = request.session.get('User')
            else:
                user_id = request.POST['USER_ID']

            with connection.cursor() as cursor:
                cursor.execute("""SELECT PurchaseID FROM Purchase 
                                WHERE PurchaseID = (SELECT MAX(PurchaseID) FROM Purchase)""")
                Max_id = cursor.fetchall()

            Purchase_ID = 1
            time_now = datetime.datetime.today()
            Total_price = int(request.POST['Amount']) * Item[0][2]

            if len(Max_id) != 0:
                Purchase_ID = Max_id[0][0] + 1
            with connection.cursor() as cursor:
                cursor.execute("INSERT Into Purchase values (%s,%s,%s,%s,%s,%s,%s,%s);",
                [Purchase_ID,ProductID,user_id,time_now,Total_price,request.POST['Requirement'],request.POST['Coupon_ID'],request.POST['Amount']])
                connection.commit()

            return HttpResponse("Your order has been processed! The Total price is %s!" % Total_price)
        else:
            return HttpResponse("That's not valid!")
    else:
        if request.session.get('User'):
            form = PurchaseForm2()
        else:
            form = PurchaseForm()
        context = {'form':form, 'ProductName': Item[0][0],
                    'ProductPrice': Item[0][2],'ProductStock': Item[0][1]}
        return render(request, 'Purchase/Purchase.html',context)

