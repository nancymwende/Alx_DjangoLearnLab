from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
    else:
        form = RegisterForm()

    return render(request, "blog/register.html", {"form": form})


@login_required
def profile(request):
    if request.method == "POST":
        request.user.email = request.POST.get("email")
        request.user.save()
        return redirect("profile")

    return render(request, "blog/profile.html")

def home(request):
    return render(request, "blog/base.html")

def login_view(request):
    return render(request, "blog/login.html")

def register_view(request):
    return render(request, "blog/register.html")

def profile_view(request):
    return render(request, "blog/profile.html")