from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_book, name='add_book'),
    path('library/', views.library, name='library'),
    path('search/', views.search, name='search'),
    path('account/', views.account, name='account'),
]
