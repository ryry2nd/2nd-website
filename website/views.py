from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate, login

prefix = "/2nd"

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/2nd/welcome")
    
    return render(request, "2ndIndex.html", {'prefix': prefix})

def cubeEquation(request):
    return render(request, "cubeEquation.html", {'prefix': prefix})

def log_in(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(f"{prefix}/welcome")
    
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(f"{prefix}/welcome")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form, 'prefix': prefix})