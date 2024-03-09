from django.shortcuts import render
from django.contrib import admin

from django.urls import path, include
from haxamoi_app import views  

from django.http import JsonResponse

#create functionality 

def home(request):
    return render(request, '')

#def dashboard(request):
    # Assuming you have user authentication
    if request.user.is_authenticated:
        return render(request, 'haxamoi_app/dashboard.html')
    else:
        return redirect('/')

def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = 'hi this is my response'
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'hexamoi.html')


def admin(request):
    return render(request, 'haxamoi_app/admin.html')   



