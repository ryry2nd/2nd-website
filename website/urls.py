from django.urls import path
from django.contrib import admin
from . import views, viewsAuth

urlpatterns = [
    path('', views.index, name='index'),
    path('admin', admin.site.urls),
    path('cubeEquation', views.cubeEquation),
    path('login', views.log_in),
    path('welcome', viewsAuth.welcome),
    path('logout', viewsAuth.log_out),
    path('fileShare', viewsAuth.fileShare),
    path('download/<path>/', viewsAuth.download),
]