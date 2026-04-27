from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'name': 'Home'})

def add_book(request):
    return render(request, 'add_book.html', {'name': 'Add Book'})

def library(request):
    return render(request, 'library.html', {'name': 'Library'})

def search(request):
    return render(request, 'search.html', {'name': 'Search'})

def account(request):
    return render(request, 'account.html', {'name': 'Account'})
