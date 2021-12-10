from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
import datetime
import hashlib

from .models import Userx
from .forms import UsersignupForm, UsersigninForm
# Create your views here.
def index(request):
    user_id = request.session.get('User')
    if user_id:
        return render(request,"index/page.html",{'user_id':user_id})
    return render(
        request, 
        "index/page.html"
    )
def logout(request):
    if request.session.get('User'):
        del(request.session['User'])
    return redirect('/')

def signup(request):
    if request.method == "POST":
        form = UsersignupForm(request.POST)
        if form.is_valid():
            with connection.cursor() as cursor:
                cursor.execute("""SELECT UserID FROM Userx 
                                WHERE UserID = %s""",[request.POST['UserID']])
                id_check = cursor.fetchall()
            if len(id_check) != 0:
                return HttpResponse("It's a duplicate ID.")
            else:
                time_now = datetime.datetime.today()
                encrypted_pw = hashlib.sha3_512(request.POST['Password'].encode()).hexdigest()
                default_grade = "Seed"
                with connection.cursor() as cursor:
                    cursor.execute("INSERT Into Userx values (%s,%s,%s,%s,%s,%s,%s,%s,%s);",
                    [request.POST['UserID'],request.POST['UserName'],encrypted_pw,request.POST['Gender'],request.POST['Age'],request.POST['Email'],request.POST['Phone'],default_grade,time_now])
                    connection.commit()
                return HttpResponse("Welcome to the new member! <br>You have succeeded in signing up")
        else:
            return HttpResponse("That's not valid!")

    else:
        form = UsersignupForm()
        return render(request, 'index/signup.html',{'form':form})

def signin(request):
    if request.method == "POST":
        form = UsersigninForm(request.POST)
        if form.is_valid():
            with connection.cursor() as cursor:
                encrypted_pw_in = hashlib.sha3_512(request.POST['Password'].encode()).hexdigest()
                cursor.execute("""SELECT UserID FROM Userx 
                                WHERE UserID = %s and Passward = %s""",[request.POST['UserID'],encrypted_pw_in])
                id_ps_check = cursor.fetchall()
            if len(id_ps_check) == 0:
                return HttpResponse("That ID doesn't exist. Sign up as a member.")
            else:
                request.session['User'] = request.POST['UserID']
                return redirect('/')
        else:
            return HttpResponse("That's not valid!")

    else:
        form = UsersigninForm()
        return render(request, 'index/signin.html',{'form':form})

        