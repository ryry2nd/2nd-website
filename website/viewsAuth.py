from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render
from django.contrib.auth import logout
import os

prefix = "/2nd"

def welcome(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(f"{prefix}")
    
    user = request.user

    return render(request, "welcome.html", {'prefix': prefix})

def log_out(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(f"{prefix}")
    
    logout(request)
    return HttpResponseRedirect(f"{prefix}")