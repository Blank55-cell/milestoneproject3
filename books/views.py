from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book

def home(request):
    return render(request, 'home.html', {'name': 'Home'})


@login_required
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        favourite_chapter = request.POST.get('favourite_chapter')
        notes = request.POST.get('notes')
        status = request.POST.get('reading_status')

        # Save the book with the logged-in user
        Book.objects.create(
            user=request.user,
            title=title,
            author=author,
            favourite_chapter=favourite_chapter,
            notes=notes,
            status=status
        )

        return redirect('library')

    return render(request, 'add_book.html', {'name': 'Add Book'})


@login_required
def library(request):
    # Only show books belonging to the logged-in user
    books = Book.objects.filter(user=request.user)
    return render(request, 'library.html', {'name': 'Library', 'books': books})


@login_required
def search(request):
    query = request.GET.get('q', '')

    if query:
        books = Book.objects.filter(user=request.user, title__icontains=query)
    else:
        books = []

    return render(request, 'search.html', {
        'name': 'Search',
        'books': books,
        'query': query
    })


@login_required
def account(request):
    return render(request, 'account.html', {'name': 'Account'})
