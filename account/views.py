from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import User
# Create your views here.
def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password_1 = request.POST.get('password1', '')
        password_2 = request.POST.get('password2', '')

        if name and email and password_1 and password_2:
            user = User.objects.create_user(name, email, password_1)
            print('User created.', user)

            return redirect('/login/')
        else:
            print('Something went wrong.')
    else:
        print("just show form")
    return render(request, 'account/signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        if email and password:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user)

                return redirect('/projects/')
        else:
            print('Something went wrong.')
    return render(request, 'account/login.html')

@login_required
def logout(request):
    auth_logout(request)

    return redirect('/')