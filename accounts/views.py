from django.shortcuts import render
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
            return JsonResponse({"success": False, "error": "All fields are required."}, status=400)

        # Make sure username/email aren't already taken
        if User.objects.filter(username__iexact=username).exists():
            return JsonResponse({"success": False, "error": "Username already taken."}, status=400)

        if User.objects.filter(email__iexact=email).exists():
            return JsonResponse({"success": False, "error": "Email already in use."}, status=400)

        # Try creating the user
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
        except IntegrityError:
            return JsonResponse({"success": False, "error": "Could not create user. Try again."}, status=500)
        except Exception:
            return JsonResponse({"success": False, "error": "Unexpected error."}, status=500)

        # Log them in right after registering
        login(request, user)
        return JsonResponse({"success": True, "redirect": "/library"})

    # GET request → show the HTML UI
    return render(request, "account.html")


# Handle login
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not email or not password:
            return JsonResponse({"success": False, "error": "Email and password required."}, status=400)

        # Look up user by email
        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            return JsonResponse({"success": False, "error": "Invalid credentials."}, status=400)

        # Django auth uses username internally
        user = authenticate(request, username=user_obj.username, password=password)

        if user is None:
            return JsonResponse({"success": False, "error": "Invalid credentials."}, status=400)

        login(request, user)
        return JsonResponse({"success": True, "redirect": "/library"})

    # GET request → show the HTML UI
    return render(request, "account.html")


# Handle logout
def logout_view(request):
    logout(request)
    return JsonResponse({"success": True, "redirect": "/"})
