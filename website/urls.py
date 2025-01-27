from django.urls import path
from . import views, viewsAuth
from django.contrib import admin

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('cubeEquation', views.cubeEquation),
    path('login', views.log_in),
    path('welcome', viewsAuth.welcome),
    path('logout', viewsAuth.log_out),
]