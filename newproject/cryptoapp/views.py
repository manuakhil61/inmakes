from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
# /////////  Login Page Code //////////////
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"username or password is wrong")
            return redirect('login')
    return render(request,'login.html')

# ////// Success page code /////////
def success(request):
    return render(request,'success.html')

# //////// Register Page Code ////////

def register(request):
    if request.method =="POST":
        username=request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists ():
                messages.info(request,"Username already in use")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already in use')
                return redirect('register')
            else:
               crypto=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
               crypto.save()
               return redirect('success')
        else:
          messages.info(request,"Password is not matching")
          return redirect('register')

        return redirect('/')
    return render(request,'register.html')

# ///////// Logout code ////////

def logout(request):
    auth.logout(request)
    return redirect('/')