from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def login(request):
    if(request.method=='POST'):
        user=auth.authenticate(username=request.POST['username'],password=request.POST['psswd'])
        if(user is not None):
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'account/login.html',{'error':'your username or passord is incorrect'})
    else:
        return render(request,'account/login.html')
def logout(request):
    if(request.method=='POST'):
        auth.logout(request)
        return redirect('home')
def signup(request):
    if(request.method=='POST'):
        if(request.POST['new_psswd']==request.POST['cnf_psswd']):
            try:
               user=User.objects.get(username=request.POST['username'])
               return render(request,'account/signup.html',{'error':'Pls choose different username,it already exists!'})
            except User.DoesNotExist:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['new_psswd'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,'account/signup.html',{'error':'Password must match!'})


    else:
        return render(request,'account/signup.html')

