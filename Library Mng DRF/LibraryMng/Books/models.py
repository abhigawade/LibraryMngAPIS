from django.db import models

# Create your models here.
class BookAuthor(models.Model):
    author = models.CharField(max_length=200, null=False)
    
    def __str__(self):
        return self.author
    
class BookCategory(models.Model):
    category = models.CharField(max_length=200, null=False)
    
    def __str__(self):
        return self.category

class Book(models.Model):    
    title = models.CharField(max_length=200, null=False)
    price = models.IntegerField(null=False)
    author = models.ManyToManyField(BookAuthor, related_name='book')
    isbn = models.CharField(max_length=200, unique=True)
    category = models.ManyToManyField(BookCategory, related_name='book')
    
    def __str__(self):
        return self.title

