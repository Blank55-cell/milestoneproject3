from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
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
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='To Read')
    cover_url = models.CharField(max_length=200, blank=True)
    google_id = models.CharField(max_length=100, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class BookCategory(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
