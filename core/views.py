from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return redirect('/projects/')
    
    return render(request, 'core/index.html')


def about(request):
    return render(request, 'core/about.html')