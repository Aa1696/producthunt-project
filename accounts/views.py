from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'account/login.html')
def logout(request):
    return render(request,'account/logout.html')
def signup(request):
    return render(request,'account/signup.html')
