from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache, cache_control


from .models import Departments, Doctors

from .forms import BookingForm

# Create your views here.

@never_cache
@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

@never_cache
def SignupPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    error_message=None
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            error_message = "The passwords you entered do not match."
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render(request,'signup.html', {'error_message': error_message})

@never_cache
def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    error_message = None
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            error_message = "Username or password is incorrect!"
    return render(request,'login.html',{'error_message': error_message})

@never_cache
@login_required(login_url='login')
def about(request):
    return render(request, 'about.html')

@never_cache
@login_required(login_url='login')
def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    form = BookingForm()
    dict_form={
        'form': form
    }
    return render(request, 'booking.html', dict_form)

@never_cache
@login_required(login_url='login')
def doctors(request):
    dict_docs={
        'doctors': Doctors.objects.all()
    }
    return render(request, 'doctors.html', dict_docs)

@never_cache
@login_required(login_url='login')
def contact(request):
    return render(request, 'contact.html')

@never_cache
@login_required(login_url='login')
def department(request):
    dict_dept={
        'dept': Departments.objects.all()
    }
    return render(request, 'department.html', dict_dept)

def LogoutPage(request):
    logout(request)
    return redirect('login')




























