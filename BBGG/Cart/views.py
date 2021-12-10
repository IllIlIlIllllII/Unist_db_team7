from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
# Create your views here.

# import cx_Oracle

# Create your views here.

def index(request):
    # please edit this
    # connection = cx_Oracle.connect(
    #     user="Jongchan",
    #     password="20141571",
    #     dsn="localhost:1521"
    # )

    try:
        buy = request.GET['buyid']
        
    except:
        buy = -1

    if buy != -1:
        # do something (e.g., db update)
        return HttpResponse("good.")


    userid = request.session.get('User')

    cursor = connection.cursor()
    cursor.execute("select * from cart where UserID = %s" % userid)
    
    rows = cursor.fetchall()
    
    # aggregation
    cursor.execute("select count(*) from cart where UserID = %s" % userid)  
    nitems = cursor.fetchall()[0]
    
    cursor.execute("select sum(productprice * amount) from cart where UserID = %s" % userid)
    try:
        total = "{:,}".format(cursor.fetchall()[0][0])
    except:
        total = 0




    msg = "some-message"
    return render(
        request, 
        "Cart/page.html",
        {
            "message": msg, 
            "msgs": ["msg1", "msg2", "msg3", "msg4", "this is last one"],
            "rows": rows,
            "total": total,
            "nitems": nitems,
            "userid": userid

        }
    )
