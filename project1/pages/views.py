from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def sample(request):
    return HttpResponse("welcome to django")


def sample1(request, name):
    return HttpResponse(name)

def sample2(request):
    return render(request,'index1.html')

def sample3(request,name):
    return render(request,'index.html',{'name':name})

def sample4(request):
    name="good morning"
    return render(request,'index.html',{'name':name})


def sample5(request):
    lst=["divyesh","hari","ram"]
    return render(request,'index2.html',{'lst':lst})


def sample6(request):
    return redirect('cp2')

def sample7(request):
    return render(request,'base.html')


def sample8(request):
    return render(request,'index4.html')

def register(request):
    username="ram"
    email="ram@gmail.com"
    fname="ram"
    User.objects.create_user(username,email,fname)
    return HttpResponse("user created successfully")