"""
Models for the books application of the Book Vault project.
Defines the structure for Books, Categories, and Reviews.
"""

from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    """
    Model representing a book added to a user's library.
    """
    STATUS_CHOICES = [
        ('To Read', 'To Read'),
        ('Reading', 'Reading'),
        ('Completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    favourite_chapter = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='To Read'
    )
    cover_url = models.CharField(max_length=200, blank=True)
    google_id = models.CharField(max_length=100, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    """
    Model representing book categories/genres.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class BookCategory(models.Model):
    """
    Linker model to associate Books with Categories.
    """
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Review(models.Model):
    """
    Model representing user reviews for specific books.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)