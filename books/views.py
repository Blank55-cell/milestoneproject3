from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from .models import Book

def home(request):
    return render(request, 'home.html', {'name': 'Home'})

@login_required
def add_book(request):
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
    books = Book.objects.filter(user=request.user)
    return render(request, 'library.html', {'name': 'Library', 'books': books})

@login_required
def search(request):
    query = request.GET.get('q', '')
    if query:
        books = Book.objects.filter(user=request.user, title__icontains=query)
    else:
        books = []
    return render(request, 'search.html', {'name': 'Search', 'books': books, 'query': query})

# We REMOVED @login_required so you can actually access the login form!
def account(request):
    # If already logged in, don't show the login page, just go home
    if request.user.is_authenticated and request.method == 'GET':
        return redirect('home')

    if request.method == 'POST':
        # REGISTRATION LOGIC: Triggered if 'username' is in the form
        if 'username' in request.POST:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            # Create user, log them in, and send to library
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return redirect('library')

        # LOGIN LOGIC: Triggered if it's the sign-in form
        else:
            # We use the 'email' field from your HTML as the 'username' for Django
            email_val = request.POST.get('email')
            pass_val = request.POST.get('password')
            
            user = authenticate(request, username=email_val, password=pass_val)
            
            if user is not None:
                login(request, user)
                return redirect('library')
            else:
                # Re-render with an error message if it fails
                return render(request, 'account.html', {'error': 'Invalid credentials'})

    return render(request, 'account.html', {'name': 'Account'})

# Added a logout view so you can sign out later
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id, user=request.user)
    book.delete()
    return redirect('library')

@login_required
def book_details(request, book_id):
    book = Book.objects.get(id=book_id, user=request.user)
    return render(request, 'book_details.html', {'book': book})