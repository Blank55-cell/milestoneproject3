from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()


def login_view(request):
    """
    Handles user login requests.
    Using email to log in, but Django still needs the username internally.
    """
    if request.method == "POST":
        email = request.POST.get("email", "").strip().lower()
        password = request.POST.get("password", "")

        if not email or not password:
            messages.error(request, "Please provide both email and password.")
            return render(request, "account.html")

        # Convert email → username
        try:
            user_obj = User.objects.get(email=email)
            username = user_obj.username
        except User.DoesNotExist:
            messages.error(request, "Invalid credentials.")
            return render(request, "account.html")

        # Authenticate using username + password
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("library")

        messages.error(request, "Invalid credentials.")
        return render(request, "account.html")

    return render(request, "account.html")


def register_view(request):
    """
    Handles new user registration.
    """
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip().lower()
        password = request.POST.get("password", "")

        if not username or not email or not password:
            messages.error(request, "All fields are required.")
            return render(request, "account.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return render(request, "account.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return render(request, "account.html")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)
        return redirect("library")

    return render(request, "account.html")


def logout_view(request):
    """
    Logs out the user and redirects to home.
    """
    logout(request)
    return redirect("home")

