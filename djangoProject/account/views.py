from django.shortcuts import render, redirect
from .forms import RegisterUserForm
from django.contrib.auth.models import User  #  قتی می خوای یوزر بسازی باید این رو ایمپرت کنی
from django.contrib import messages
from .forms import LoginUserForm
from django.contrib.auth import authenticate, login    #  وقتی می خوای اکانت کاربر رو وارد کنی باید این رو ایمپرت کنی
from django.contrib.auth import logout

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password'])  #  این موارد از قبل توی فرم بودن
            messages.success(request, 'Account created successfully', 'success')
            return redirect('home')
    elif request.method == 'GET':
        form = RegisterUserForm()
    return render(request, 'register.html', {"form": form})

def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data # اطلاعات وارد شده رو میگیره
            user = authenticate(request, username=cd['username'], password=cd['password'])  # بررسی می کنه که username password کاربروجود داشته باشه
            if user is not None:  #  گر کاربر وجود داشت
                login(request, user)
                messages.success(request, 'Login successful', 'success')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password', 'danger')
    else:
        form = LoginUserForm()
    return render(request, 'login.html', {"form": form})

def logout_user(request):  #  طریقه بیرون انداختن کاربر
    logout(request)
    messages.success(request, 'Logged out successfully', 'success')
    return redirect('home')