from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.db import connection

from .models import Purchase

# Create your views here.

def index(request,ProductID):
    with connection.cursor() as cursor:
        cursor.execute("SELECT ProductID FROM ProductList_Product WHERE ProductID =%s",[ProductID])
        Product = cursor.fetchall()
    if len(Product) == 0:
        raise Http404("The product does not exist.")
    return HttpResponse("You're looking at Product %s." % Product )