from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def login(request):
    return render(request,'account/login.html')
def logout(request):
    return render(request,'account/logout.html')
def signup(request):
    if(request.method=='POST'):
        if(request.POST['new_psswd']==request.POST['cnf_psswd']):
            try:
               user=User.objects.get(username=request.POST['username'])
               return render(request,'account/signup.html',{'error':'User already enrolled!'})
            except User.DoesNotExist:
                user=User.objects.create_user(username=request.POST['username'],password=User.objects.get(username=request.POST['new_psswd']))
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,'account/signup.html',{'error':'Password must match!'})


    else:
        return render(request,'account/signup.html')

