from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth import login  ,authenticate ,logout
from django.contrib.auth.models import User 
from django.contrib import messages
# Create your views here.
from django import urls 
def home (request):
    return render(request,"index.html")

def signin(request):

    if request.method =="POST" :
        username = request.POST['uname']
        password = request.POST['pass']
        user = authenticate(username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return render(request,"index.html")
    return render(request,"login.html")

def signout(request):
    logout(request)
    return render(request,"login.html")

def register(request):

    if request.method == "POST":
        data = request.POST
        if data["password1"] == data["password2"] : 
            user = User()
            user.username = data["uname"]
            user.email = data["email"]
            user.set_password(data["password1"])
            user.save()
        else:
            messages.error(request,"Password Mismatch ")

    return render(request,"register.html")