
from django.contrib import admin
from django.urls import path
from visual import views

from django.urls import path, include
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), 
    path('home/', views.home, name='home'),
    path('continuar/', views.home, name='home'),
]