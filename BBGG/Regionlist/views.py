from django.shortcuts import render
from django.http import HttpResponse

import cx_Oracle

# Create your views here.

def index(request):

    connection = cx_Oracle.connect(
        user="system",
        password="dmstjd12",
        dsn="localhost:1521"
    )

    # region code
    # 0: entire
    # 1: Seoul
    # 2: ...
    qry_to_region = [
        ""
    ]

    qry = "all"
    try:
        qry = request.GET['qry']
    except:
        pass

    


    cursor = connection.cursor()
    # TODO: filter by qry (where region = qry)
    cursor.execute("select * from AAA") 

    rows = cursor.fetchall()
    


    msg = "some-message"
    return render(
        request, 
        "Regionlist/page.html",
        {
            "message": msg, 
            "msgs": ["msg1", "msg2", "msg3", "msg4", "this is last one"],
            "rows": rows,
            "qry": qry,
        }
    )