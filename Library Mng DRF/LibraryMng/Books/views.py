from django.shortcuts import render
from .models import Book, BookAuthor, BookCategory
from .serializers import BookSerializer, BookAuthorSerializer, BookCategorySerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import BasicAuthentication

# Create your views here.

class BookModelViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    
class BookAuthorModelViewSet(viewsets.ModelViewSet):
    serializer_class = BookAuthorSerializer
    queryset = BookAuthor.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

class BookCategoryModelViewSet(viewsets.ModelViewSet):
    serializer_class = BookCategorySerializer
    queryset = BookCategory.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]