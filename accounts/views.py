# Handle login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_view(request):
    """
    Handles user login requests.
    """
    if request.method == "POST":
        email = request.POST.get("email", "").strip().lower()
        password = request.POST.get("password", "")

        if not email or not password:
            messages.error(request, "Please provide both email and password.")
            return render(request, "login.html")

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials.")

    return render(request, "login.html")


def register_view(request):
    """
    Handles new user registration.
    """
    return render(request, "register.html")


def logout_view(request):
    """
    Logs out the user and redirects to home.
    """
    logout(request)
    return redirect('home')