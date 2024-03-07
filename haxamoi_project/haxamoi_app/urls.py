from django.urls import path
from django.contrib import admin
from haxamoi_app import views  # This line imports views from your haxamoi_app


urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin/', admin.site.urls),
    path('chat/', views.chat, name='chat'),
]

