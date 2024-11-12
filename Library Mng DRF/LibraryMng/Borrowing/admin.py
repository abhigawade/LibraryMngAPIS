from django.contrib import admin
from .models import Borrow
# Register your models here.

@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'borrow_date', 'due_date', 'return_date')
    search_fields = ('user', 'book')