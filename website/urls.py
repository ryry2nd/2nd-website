from django.urls import path
from django.contrib import admin
from . import views, viewsAuth

urlpatterns = [
    path('', views.index, name='index'),
    path('admin', admin.site.urls),
    path('cubeEquation', views.cubeEquation, name='cubeEquation'),
    path('login', views.log_in, name='login'),
    path('welcome', viewsAuth.welcome, name='welcome'),
    path('logout', viewsAuth.log_out, name='logout'),
    path('fileShare', viewsAuth.fileShare, name='fileShare')
]