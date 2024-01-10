from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render
from django.contrib.auth import logout
import os

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
    
    return render(request, "fileShare.html", {"files": os.listdir(os.environ.get("DOWNLOAD_PATH"))})

def download(request, path):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/")
    
    file_path = os.path.join(os.environ.get("DOWNLOAD_PATH"), path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404