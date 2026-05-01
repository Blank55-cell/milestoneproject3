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

        # grabbing the chapter field from the form (this matches the HTML name)
        favourite_chapter = request.POST.get('chapter')

        notes = request.POST.get('notes')

        # same thing here, just pulling the status straight from the form
        status = request.POST.get('status')

        # Save the book with the logged-in user
        Book.objects.create(
            user=request.user,
            title=title,
            author=author,
            favourite_chapter=favourite_chapter,
            notes=notes,
            status=status
        )

        # once the book is saved, just send me back to the library page
        return redirect('library')

    return render(request, 'add_book.html', {'name': 'Add Book'})


@login_required
def library(request):
    print("Current user:", request.user)  # TEMP check
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


@login_required
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id, user=request.user)
    book.delete()
    return redirect('library')

@login_required
def book_details(request, book_id):
    book = Book.objects.get(id=book_id, user=request.user)
    return render(request, 'book_details.html', {'book': book})
