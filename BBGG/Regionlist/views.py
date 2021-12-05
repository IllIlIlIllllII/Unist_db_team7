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

    qry = "all"
    try:
        qry = request.GET['qry']
    except:
        pass


    cursor = connection.cursor()
    # region querystring
    cursor.execute("select * from region where regionname = '%s'" % str(qry)) 
    res = cursor.fetchall()
    
    try:
        desc = res[0][2]
    except:
        desc = "No description"


    if qry == "all":
        cursor.execute("select * from Product")
    else:
        cursor.execute("select * from Product where productregion = '%s'" % str(qry))

    items = cursor.fetchall()

    msg = "some-message"
    
    return render(
        request, 
        "Regionlist/page.html",
        {
            "message": msg, 
            "msgs": ["msg1", "msg2", "msg3", "msg4", "this is last one"],
            "desc": desc,
            "qry": qry,
            "items": items,
        }
    )