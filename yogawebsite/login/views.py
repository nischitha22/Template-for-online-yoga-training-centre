from django.shortcuts import render

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
import mysql.connector as sql
from django.http import HttpResponse


emails=''
passwds=''


# Create your views here.


def login(request):
    global emails, passwds
    
    if request.method=="POST" :
        m=sql.connect(host="localhost", user="root", passwd="Niss#0922", database='yogaweb')
        cursor=m.cursor()
        d=request.POST
        for key, value in d.items() :
            if key=="email":
                emails=value
            if key=="password":
                passwds=value
        c="select * from users where email='{}' and password='{}'".format(emails,passwds)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return HttpResponse('error')
        else :
            return render(request,'users/home2.html')
    return render(request, 'users/login.html')
        
    
    
# Create your views here.
