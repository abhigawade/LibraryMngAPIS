from django.shortcuts import render
from .models import Borrow
from .serializers import BorrowSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.authentication import BasicAuthentication

# Create your views here.
class BorrowModelView(viewsets.ViewSet):
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        borrows = Borrow.objects.all()
        serializer = BorrowSerializer(borrows, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        borrow = Borrow.objects.get(pk=pk)
        serializer = BorrowSerializer(borrow)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = BorrowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        borrow = Borrow.objects.get(pk=pk)
        serializer = BorrowSerializer(borrow, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
    def destroy(self, request, pk=None):
        borrow = Borrow.objects.get(pk=pk)
        borrow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)