from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from .forms import UpdateUser
from django.db import IntegrityError

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def signup(request):
    if request.user.is_authenticated:
        return redirect("home_page")
    
    if request.method == 'POST':
        input_username = request.POST['username']
        input_password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if not input_username or not input_password or not confirm_password:
            messages.error(request, 'Enter username, password, and confirm password')
            return render(request, 'signup.html')
        
        if User.objects.filter(username=input_username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'signup.html')

        try:
            objUser = User.objects.create_user(username=input_username, password=input_password)
            objUser.save()
            messages.success(request,'your account has created succesfully')
            return redirect('login_page')
        except IntegrityError:
            messages.error(request, 'An error occurred. Please try again.')
            return render(request, 'signup.html')
    
    return render(request, 'signup.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    if request.user.is_authenticated:
        return redirect("home_page")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not username or not password:
            messages.error(request, 'Enter username and password')
            return render(request, 'login.html')
        user = authenticate(request, username=username, password=password,)
        if user is not None:
            if user.is_superuser:
                messages.error(request, 'Invalid username or password')
                return redirect('login_page')
            else:
                request.session['user_id'] = user.id
                auth_login(request, user)
                return redirect('home_page')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

@login_required(login_url='login_page')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    if not request.user.is_authenticated:
        return redirect("login_page")
    user_id = request.session['user_id']
    user = User.objects.get(id=user_id)
    username = user.username
    if user.is_superuser:
        return redirect('adminDashboard')
    return render(request, 'home.html', {'username': username})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def adminlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not username or not password:
            messages.error(request, 'Enter username and password')
            return render(request, 'adminlogin.html')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            request.session['user_id'] = user.id
            auth_login(request, user)
            return redirect('adminDashboard')
        else:
            messages.error(request, 'Invalid Admin ID or password')
            return render(request, 'adminlogin.html')
    return render(request, 'adminlogin.html')

@login_required(login_url='adminlogin')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def adminDashboard(request):
    if not request.user.is_superuser:
        return redirect('home_page') 
    user_set = User.objects.filter(is_superuser=False)
    admin_id = request.session.get('user_id')
    if admin_id:
        admin = User.objects.get(id=admin_id)
        admin_name = admin.username
        return render(request, 'adminDashboard.html', {'userlist': user_set, 'admin_name': admin_name})
    else:
        return redirect('adminlogin') 

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def edit(request, pk):
    user_to_be_editted = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateUser(request.POST, instance=user_to_be_editted)
        if form.is_valid():
            form.save()
            return redirect('adminDashboard')
    else:
        form = UpdateUser(instance=user_to_be_editted)
    return render(request, 'edit.html', {'form': form, 'user': user_to_be_editted})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def delete(request, pk):
    if request.method == 'POST':
        instance = User.objects.get(pk=pk)
        instance.delete()
        # messages.success(request, 'User deleted successfully.')
    else:
        messages.error(request, 'Invalid request method.')
    return redirect('adminDashboard')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def signout(request):
    logout(request)
    return redirect('login_page')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def adminsignout(request):
    logout(request)
    return redirect('adminlogin')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def search(request):
    user_set = User.objects.none() 
    if 'keyword' in request.GET:
        keyword = request.GET.get('keyword', '')
        user_set = User.objects.filter(username__icontains=keyword, is_superuser=False)
    
    context = {
        'userlist': user_set,
    }
    return render(request, 'adminDashboard.html', context)