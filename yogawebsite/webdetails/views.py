
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
import mysql.connector as sql
from django.http import HttpResponse
name=''
emailaddress=''
ph=''
mg=''
un=''
emails=''
passwds=''
def about(request):
    return render(request, 'users/about.html')
def classes(request):
    return render(request, 'users/classes.html')
def home2(request):
    return render(request, 'users/home2.html')
def contact(request):
    global name, emailaddress, ph, mg
    if request.method=="POST" :
        r=sql.connect(host="localhost", user="root", passwd="Niss#0922", database='yogaweb')
        cursor=r.cursor()
        f=request.POST
        for key, value in f.items() :
            if key=="name":
                name=value
            
            if key=="phone":
                ph=value
            if key=="emailadd":
                emailaddress=value
            if key=="msg":
                mg=value

        l="insert into enquiries Values('{}', '{}', '{}', '{}')".format(name,ph,emailaddress,mg)
        cursor.execute(l)
        r.commit()
    
    return render(request, 'users/contact.html')

def result(request):
    names=request.POST['un']
    return render(request, 'users/home2.html', {'answer':names})
# Create your views here.
def home(request):
    return render(request, 'users/index.html')

def register(request):
    global un, emails, passwds
    if request.method=="POST" :
        m=sql.connect(host="localhost", user="root", passwd="Niss#0922", database='yogaweb')
        cursor=m.cursor()
        d=request.POST
        for key, value in d.items() :
            if key=="username":
                un=value
            if key=="email":
                emails=value
            if key=="password":
                passwds=value
        c="insert into users Values('{}', '{}', '{}')".format(un,emails,passwds)
        cursor.execute(c)
        m.commit()
    
        
    
    return render(request, 'users/register.html')