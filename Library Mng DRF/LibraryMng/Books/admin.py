from django.contrib import admin
from .models import Book, BookAuthor, BookCategory

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'isbn')
    search_fields = ('title', 'isbn')
    
@admin.register(BookAuthor)
class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ('author',)
    search_fields = ('author',)

@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)    
    search_fields = ('category',)