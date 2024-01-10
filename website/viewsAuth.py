from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import logout

def welcome(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/")
    
    user = request.user

    return render(request, "welcome.html")

def log_out(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/")
    
    logout(request)
    return HttpResponseRedirect("/")

def fileShare(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/")
    
    return render(request, "fileShare.html")