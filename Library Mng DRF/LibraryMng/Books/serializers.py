from rest_framework import serializers
from .models import Book, BookAuthor, BookCategory

class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAuthor
        fields = ('id','author',)

class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = ('id','category',)

class BookSerializer(serializers.ModelSerializer):
    author = BookAuthorSerializer(many=True)
    category = BookCategorySerializer(many=True)
    
    class Meta:
        model = Book
        fields = ('id','title', 'price', 'author', 'isbn', 'category')
        
    def create(self, validated_data):
        authors_data = validated_data.pop('author')
        categories_data = validated_data.pop('category')
        
        book = Book.objects.create(**validated_data)
        
        for author_data in authors_data:
            author, _ = BookAuthor.objects.get_or_create(**author_data)
            book.author.add(author)
        
        
        for category_data in categories_data:
            category, _ = BookCategory.objects.get_or_create(**category_data)
            book.category.add(category)
        
        return book
    
    
    def update(self, instance, validated_data):
        authors_data = validated_data.pop('author')
        categories_data = validated_data.pop('category')
        
        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.isbn = validated_data.get('isbn', instance.isbn)
        
        instance.save()
        
        for author_data in authors_data:
            author, _ = BookAuthor.objects.get_or_create(**author_data)
            instance.author.add(author)
        
        
        for category_data in categories_data:
            category, _ = BookCategory.objects.get_or_create(**category_data)
            instance.category.add(category)        
        
        return instance