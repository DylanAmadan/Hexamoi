from django.shortcuts import render

from django.contrib import admin
from django.urls import path, include
from haxamoi_app import views  


#create functionality 

def home(request):
    return render(request, 'hexamoi.html')

#def dashboard(request):
    # Assuming you have user authentication
    if request.user.is_authenticated:
        return render(request, 'haxamoi_app/dashboard.html')
    else:
        return redirect('/')

def chat(request):
    return render(request, 'hexamoi.html')
    if request.method == 'POST':
        message = request.POST.get('message')
        print(message)

def admin(request):
    return render(request, 'haxamoi_app/admin.html')   


