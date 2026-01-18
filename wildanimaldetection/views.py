
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from  django.core.files.storage import FileSystemStorage
import datetime

from .models import *
import os
#from ML import test

def first(request):
    return render(request,'index.html')

def index(request):
    return render(request,'index.html')

def register(request):
    return render(request,'register.html')

def registration(request):
    if request.method=="POST":
        name=request.POST.get('name')
        place=request.POST.get('place')
        email=request.POST.get('email')
        password=request.POST.get('password')
        reg=registerr(name=name,place=place,email=email,password=password)
        reg.save()
        return render(request,'index.html',{'status': 'Register Successfully'})

def login(request):
    return render(request,'login.html')

def addlogin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if email=='admin@gmail.com' and password =='admin':
        request.session['logint']=email
        request.session['role']='admin'
        return render(request,'index.html')
    elif registerr.objects.filter(email=email,password=password).exists():
        var=registerr.objects.get(email=email, password=password)
        request.session['user_id']=var.id
        return render(request,'index.html')
    else:
        return render(request, 'login.html', {'status': 'invalid email or password'})

def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(first)

def v_users(request):
  
    users=registerr.objects.all()
    return render(request,'v_users.html',{'users':users})
 