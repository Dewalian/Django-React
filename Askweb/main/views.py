from . forms import RegisterForm
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
def home(request):
    return HttpResponse("Test")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("/home")
    else:
        form = RegisterForm()
    return HttpResponse("nice")

