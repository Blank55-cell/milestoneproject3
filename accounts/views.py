from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.http import JsonResponse
from django.db import IntegrityError

User = get_user_model()

# Basic account page
def account_page(request):
    return render(request, "account.html")


# Handle user registration
def register_view(request):
    if request.method == "POST":
        data = request.POST
        username = (data.get("username") or "").strip()
        email = (data.get("email") or "").strip().lower()
        password = data.get("password")

        # Quick checks
        if not username or not email or not password:
            return render(request, "account.html", {"error": "All fields are required."})

        # Make sure username/email aren't already taken
        if User.objects.filter(username__iexact=username).exists():
            return render(request, "account.html", {"error": "Username already taken."})

        if User.objects.filter(email__iexact=email).exists():
            return render(request, "account.html", {"error": "Email already in use."})

        # Try creating the user
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            # Log them in right after registering
            login(request, user)
            return redirect('library')
        except IntegrityError:
            return render(request, "account.html", {"error": "Could not create user. Try again."})
        except Exception:
            return render(request, "account.html", {"error": "Unexpected error."})

    # GET request → show the HTML UI
    return render(request, "account.html")


# Handle login
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not email or not password:
            return render(request, "account.html", {"error": "Email and password required."})

        # Look up user by email
        try:
            user_obj = User.objects.get(email=email)
            # Django auth uses username internally
            user = authenticate(request, username=user_obj.username, password=password)

            if user is not None:
                login(request, user)
                return redirect('library')
            else:
                return render(request, "account.html", {"error": "Invalid credentials."})
        except User.DoesNotExist:
            return render(request, "account.html", {"error": "Invalid credentials."})

    # GET request → show the HTML UI
    return render(request, "account.html")


# Handle logout
def logout_view(request):
    logout(request)
    return redirect('home')