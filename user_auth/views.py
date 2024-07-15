
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def start_login(request):
    return render(request, "user_auth/login.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/home/")
        else:
            return redirect("/user_auth/")

def start_signup(request):
    return render(request, "user_auth/signup.html")

def signup_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if password != confirm_password or User.objects.filter(username=username) == username:
            return HttpResponse("does already exist")
        else:
            User.objects.create_user(username, email, password)
            return redirect("/user_auth/")
    else:
        return HttpResponse("there was an error")

def start_lost_password(request):
    render(request, "lost_password.html")

def logout_user(request):
    logout(request)
    return redirect("/user_auth/")
