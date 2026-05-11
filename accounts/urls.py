from django.contrib import admin
from django.urls import path, include

# Main URL configuration for the BookVault project
urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Connecting the books app for the main library features
    path('', include('books.urls')),
    
    # I'm including the accounts app urls here so register and login work properly
    path('', include('accounts.urls')),
]