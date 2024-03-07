from django.shortcuts import render

from django.contrib import admin
from django.urls import path, include
from haxamoi_app import views  


def home(request):
    return render(request, 'haxamoi_app/home.html')

def dashboard(request):
    # Assuming you have user authentication
    if request.user.is_authenticated:
        return render(request, 'haxamoi_app/dashboard.html')
    else:
        return redirect('/')

def chat(request):
    return render(request, 'haxamoi_app/chat.html')

def admin(request):
    return render(request, 'haxamoi_app/admin.html')   


