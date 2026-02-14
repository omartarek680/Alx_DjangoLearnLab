from django.shortcuts import render
from rest_framework import generics
from .models import Author, Book
from .serializers import BookSerializer, AuthorSerializer

class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateAPIView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDeleteAPIView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer