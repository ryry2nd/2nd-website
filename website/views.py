from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def cubeEquation(request):
    return render(request, "cubeEquation.html")

def login(request):
    return render(request, "login.html")