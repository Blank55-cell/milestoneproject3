from django.shortcuts import render

# Create your views here.

from django.contrib.auth import get_user_model, authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError

User = get_user_model()

def account_page(request):
    return render(request, "account.html")

def register_view(request):
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")

    if not username or not email or not password:
        return JsonResponse({"success": False, "error": "All fields are required"})

    if User.objects.filter(email=email).exists():
        return JsonResponse({"success": False, "error": "Email already in use"})

    print("Creating user with password:", password)

    user = User.objects.create_user(username=username, email=email, password=password)

    return JsonResponse({"success": True, "redirect": "/library"})



def register_view(request):
    data = _get_request_data(request)
    username = (data.get("username") or "").strip()
    email = (data.get("email") or "").strip().lower()
    password = data.get("password")

    if not username or not email or not password:
        return JsonResponse({"success": False, "error": "All fields are required."}, status=400)

    if User.objects.filter(username__iexact=username).exists():
        return JsonResponse({"success": False, "error": "Username already taken."}, status=400)

    if User.objects.filter(email__iexact=email).exists():
        return JsonResponse({"success": False, "error": "Email already in use."}, status=400)

    valid, msg = _validate_password(password)
    if not valid:
        return JsonResponse({"success": False, "error": msg}, status=400)

    try:
        user = User.objects.create_user(username=username, email=email, password=password)
    except IntegrityError:
        return JsonResponse({"success": False, "error": "Could not create user. Try again."}, status=500)
    except Exception:
        return JsonResponse({"success": False, "error": "Unexpected error."}, status=500)

    login(request, user)
    return JsonResponse({"success": True, "redirect": "/library"})
     

