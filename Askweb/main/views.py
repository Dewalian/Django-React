from . forms import RegisterForm
from django.contrib.auth import authenticate, login
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
def home(request):
    return HttpResponse("Test")

def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")
        else:
            return redirect("/register")
        
    return render(request, "register.html", {"form": form})

def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    
    user = authenticate(request, username=username, password=password)

    if user != None:
        login(request, user)
        return redirect("home")

    return render(request, "login.html", {})
