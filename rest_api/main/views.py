from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializers
from django.shortcuts import get_object_or_404


# Create your views here.

class BookListView(APIView):
    def get(self,request,pk=None):
        if pk is not None:
            Books=get_object_or_404(Book,pk=pk)
            serializer=BookSerializers(Books)
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        Books=Book.objects.all()
        serializer=BookSerializers(Books,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    
    def post(self,request):
        serializer=BookSerializers(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return  Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        if pk is None:
            return Response({"error": "No primary key provided"}, status=status.HTTP_400_BAD_REQUEST)

        Books = get_object_or_404(Book, pk=pk)
        serializer = BookSerializers(Books, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        