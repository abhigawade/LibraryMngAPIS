from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookModelViewSet, BookAuthorModelViewSet, BookCategoryModelViewSet

round = DefaultRouter()
round.register(r'book', BookModelViewSet, basename='book')
round.register(r'bookauthor', BookAuthorModelViewSet, basename='bookauthor')
round.register(r'bookcategory', BookCategoryModelViewSet, basename='bookcategory')

urlpatterns = [
    path('', include(round.urls)),
]