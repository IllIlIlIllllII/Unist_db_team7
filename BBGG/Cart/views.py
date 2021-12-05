from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

import cx_Oracle

# Create your views here.

def index(request):
    # please edit this
    connection = cx_Oracle.connect(
        user="system",
        password="dmstjd12",
        dsn="localhost:1521"
    )

    cursor = connection.cursor()
    cursor.execute("select * from cart where UserID = 1")
    
    rows = cursor.fetchall()
    
    # aggregation
    cursor.execute("select count(*) from cart where UserID = 1")  
    nitems = cursor.fetchall()[0]
    
    cursor.execute("select sum(productprice * amount) from cart where UserID = 1000")  
    total = "{:,}".format(cursor.fetchall()[0][0])
    




    msg = "some-message"
    return render(
        request, 
        "Cart/page.html",
        {
            "message": msg, 
            "msgs": ["msg1", "msg2", "msg3", "msg4", "this is last one"],
            "rows": rows,
            "total": total,
            "nitems": nitems

        }
    )