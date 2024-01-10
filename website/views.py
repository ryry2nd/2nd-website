from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/welcome")
    
    return render(request, "index.html")

def cubeEquation(request):
    return render(request, "cubeEquation.html")

def log_in(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/welcome")
    
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/welcome")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})