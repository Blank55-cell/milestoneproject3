from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

