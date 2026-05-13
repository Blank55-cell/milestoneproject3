from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Configuration for the Book model in the admin panel.
    """
    list_display = ('title', 'author', 'status', 'date_added')  # Columns shown in the list view
    search_fields = ('title', 'author')         # Adds a search bar to the admin
    list_filter = ('status',)                    # Adds a filter sidebar