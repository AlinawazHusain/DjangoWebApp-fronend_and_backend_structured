from django.shortcuts import render
from datetime import datetime
from myapp.models import Data

def index(request):
    return render (request,'index.html')

def about(request):
    return render (request,'about.html')

def contact (request):
    if request.method=="POST":
        name=request.POST.get("name")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        order=request.POST.get("order")
        data=Data(name=name,phone=phone,email=email,order=order,date=datetime.today())
        data.save()
    return render (request,'contact.html')

