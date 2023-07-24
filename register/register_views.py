from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib  import messages
from .forms import *
from .models import *
from django.http import HttpResponseRedirect


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
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        if CustomUser.objects.filter(username=username).exists():
            
            messages.error(request, 'Username is already taken.')
            return redirect('/register/')

        user = CustomUser.objects.create(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name
                )
        user.set_password(password)  
        user.save()

        
        messages.success(request, 'User registered successfully.')
        return redirect('/login/')
    else:
        return render(request, 'register.html')




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
