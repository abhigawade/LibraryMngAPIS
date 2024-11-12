from django.shortcuts import render
from rest_framework import viewsets, status
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response

# Create your views here.
class  UserView(viewsets.ViewSet):
    def list(self, request):
        data = User.objects.all()
        serializer = UserSerializer(data, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        data = User.objects.get(pk=pk)
        serializer = UserSerializer(data)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, pk=None):
        data = User.objects.get(pk=pk)
        serializer = UserSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        data = User.objects.get(pk=pk)
        data.delete()
        return Response(status=204)