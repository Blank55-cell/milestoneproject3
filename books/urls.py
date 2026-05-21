from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_book/', views.add_book, name='add_book'),
    path('library/', views.library, name='library'),
    path('search/', views.search, name='search'),
    path('account/', views.account, name='account'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('book/<int:book_id>/', views.book_details, name='book_details'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
]
