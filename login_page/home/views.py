from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
# Create your views here.

@never_cache
@login_required(login_url='login')
def index(request):
    user=request.user
    return render(request, 'index.html', {'user': user})

from django.contrib.auth.models import User

@never_cache
def SignupPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    error_message = None
    uname = ''
    email = ''
    pass1 = ''
    pass2 = ''
    
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        
        if pass1 != pass2:
            error_message = "The passwords you entered do not match."
        else:
            if User.objects.filter(username=uname).exists():
                error_message = "Username is already taken. Please choose another one."
            elif User.objects.filter(email=email).exists():
                error_message = "Email is already taken. Please use another email."
            else:
                my_user = User.objects.create_user(uname, email, pass1)
                my_user.save()
                return redirect('login')
    
    return render(request, 'signup.html', {'error_message': error_message, 'username': uname, 'email': email, 'password1': pass1, 'password2': pass2})


@never_cache
def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    error_message = None
    username = ''
    pass1 = ''
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            error_message = "Username or password is incorrect!"
    return render(request,'login.html',{'error_message': error_message, 'username': username,'password': pass1})

def LogoutPage(request):
    logout(request)
    return redirect('login')

def ContactPage(request):
    names={
        'name1':['Amal','akshay','rohan']
    }
    return render(request,'contact.html', names)