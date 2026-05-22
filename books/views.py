"""
Views for the books application of the Book Vault project.
Handles library management, book searching, and book editing.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book


def home(request):
    """
    Render the home page of the Book Vault application.
    """
    return render(request, 'home.html', {'name': 'Home'})


@login_required
def add_book(request):
    """
    Handle the addition of a new book to the user's library.
    """
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        favourite_chapter = request.POST.get('chapter')
        notes = request.POST.get('notes')
        status = request.POST.get('status')

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
    """
    Display a list of all books belonging to the logged-in user.
    """
    books = Book.objects.filter(user=request.user)
    return render(request, 'library.html', {
        'name': 'Library',
        'books': books
    })


@login_required
def search(request):
    """
    Search the user's library for books matching a title query.
    """
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
def delete_book(request, book_id):
    """
    Delete a specific book from the user's library.
    """
    book = get_object_or_404(Book, id=book_id, user=request.user)
    book.delete()
    return redirect('library')


@login_required
def book_details(request, book_id):
    """
    Display the full details of a specific book.
    """
    book = get_object_or_404(Book, id=book_id, user=request.user)
    return render(request, 'book_details.html', {'book': book})


@login_required
def edit_book(request, book_id):
    """
    Handle the modification of an existing book's details.
    """
    book = get_object_or_404(Book, id=book_id, user=request.user)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.favourite_chapter = request.POST.get('chapter')
        book.notes = request.POST.get('notes')
        book.status = request.POST.get('status')
        book.save()
        return redirect('book_details', book_id=book.id)

    return render(request, 'edit_book.html', {
        'name': 'Edit Book',
        'book': book
    })
