from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Datas
# Create your views here.

def home(request):
    
    mydata = Datas.objects.all() 
    if(mydata !=''):
         return render(request,"home4.html",{'datas':mydata})
 # return HttpResponse("<h1>Welcome to Django!!!!!!!</h1>") 
    else: 
     return render(request,"home4.html",{'Name':'Django'})

def addData(request):
    if request.method=='POST':
        name =request.POST['name']
        age =request.POST['age']
        address =request.POST['address']
        contact =request.POST['contact']
        mail =request.POST['mail']

        obj = Datas()
        obj.Name=name
        obj.Age=age
        obj.Address=address
        obj.Contact=contact
        obj.Mail=mail
        obj.save()
         
        mydata = Datas.objects.all() 
        return redirect('home') 
    return render(request,'home4.html')   

def updateData(request,id):  
              # 127.0.0.0.1:8000/updateData
    mydata=Datas.objects.get(id=id) 
    if request.method=='POST':
        name =request.POST['name']
        age =request.POST['age']
        address =request.POST['address']
        contact =request.POST['contact']
        mail =request.POST['mail']
        mydata.Name=name
        mydata.Age=age
        mydata.Address=address
        mydata.Contact=contact
        mydata.Mail=mail
        mydata.save()

        return redirect('home')


    return render(request,'update.html',{'data':mydata})

def deleteData(request,id):
    mydata=Datas.objects.get(id=id)
    mydata.delete()
    return redirect('home')


def product(request):
    mb = int(request.GET["mobile"])
    kw = int(request.GET["keyboard"])
    mo = int(request.GET["monitor"])
    price = mb+kw+mo
    return render(request,"result.html",{'Price':price})

def register(request):
    nm = request.POST['name']
    pw = request.POST['password'] 
    ad = request.POST['address'] 
    ma = request.POST['mail']  

    return render(request,"output.html",{'Name':nm,'Password':pw,'Address':ad,'Mail':ma})