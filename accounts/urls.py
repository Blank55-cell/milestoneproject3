from django.urls import path
from . import views

# These are the actual routes for my accounts app
urlpatterns = [
    path('', views.login_view, name='account_home'),
    # This points to the page where users sign up
    path('register/', views.register_view, name='register'),

    # This points to the logic for signing in
    path('login/', views.login_view, name='login'),

    # This points to the logic for logging out
    path('logout/', views.logout_view, name='logout'),
]
