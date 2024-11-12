from rest_framework import serializers
from .models import Borrow
from Users.models import User
from Books.models import Book
from Users.serializers import UserSerializer
from Books.serializers import BookSerializer

class BorrowSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    book = BookSerializer()
    
    class Meta:
        model = Borrow
        fields = ('id', 'user', 'book', 'borrow_date', 'due_date', 'return_date')
        
    def create(self, validated_data):
        users_data = validated_data.pop('user')
        books_data = validated_data.pop('book')
        
        borrow = Borrow.objects.create(**validated_data)
        
        for user_data in users_data:
            user, _ = User.objects.get_or_create(**user_data)
            borrow.user.add(user)
        
        
        for book_data in books_data:
            book, _ = Book.objects.get_or_create(**book_data)
            borrow.book.add(book)
        
        return borrow
        
    def update(self, instance, validated_data):
        users_data = validated_data.pop('user')
        books_data = validated_data.pop('book')
        
        instance.borrow_date = validated_data.get('borrow_date', instance.borrow_date)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.return_date = validated_data.get('return_date', instance.return_date)
        
        instance.save()
        
        for user_data in users_data:
            user, _ = User.objects.get_or_create(**user_data)
            instance.user.add(user)
        
        
        for book_data in books_data:
            book, _ = Book.objects.get_or_create(**book_data)
            instance.book.add(book)        
        
        return instance
    