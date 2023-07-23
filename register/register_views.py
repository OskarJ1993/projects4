from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib  import messages
from .forms import *
from .models import *

#to Render Register User Page
def register_view(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        print()
        if form.is_valid():
            user = form.save()
            user.email = form.cleaned_data['email']
            user.save()
            return redirect('login')
    else:
        form = UserCreateForm()
    return render(request, 'register.html', {'form': form})
# To create Register User
def register_add(request):
    if request.method == 'POST':
        usernamedata = request.POST['username']
        passworddata = request.POST['password']
        emaildata = request.POST['email']
        first_namedata = request.POST['first_name']
        last_namedata = request.POST['last_name']
        checkuser  = CustomUser.objects.filter(username=usernamedata)
        if checkuser.exists():
            messages.info(request,'User Name Already Exist.')
            return redirect('register')

        user = CustomUser.objects.create(username=usernamedata,first_name=first_namedata,last_name=last_namedata,email=emaildata);
        user.set_password(passworddata)
        user.save()
        return redirect('login')
    else:
        form = UserCreateForm()
    return render(request, 'register.html', {'form': form})

# TO Render Login Page and Authenticate Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials.'})
    else:
        return render(request, 'login.html')
