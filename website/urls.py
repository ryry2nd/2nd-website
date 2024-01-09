from django.urls import path
from . import views, viewsAuth

urlpatterns = [
    path('', views.index, name='index'),
    path('cubeEquation', views.cubeEquation, name='cubeEquation'),
    path('login', views.login, name='login'),
    path('welcome', viewsAuth.welcome, name='welcome'),
    path('logout', viewsAuth.log_out, name='logout'),
]