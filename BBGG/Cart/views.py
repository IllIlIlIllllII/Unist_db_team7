from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

import cx_Oracle

# Create your views here.

def index(request):

    connection = cx_Oracle.connect(
        user="system",
        password="dmstjd12",
        dsn="localhost:1521"
    )

    cursor = connection.cursor()
    cursor.execute("select * from AAA") 

    rows = cursor.fetchall()
    # TODO: aggregation
    total = "{:,}".format(12345679)    
    nitems = 111


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