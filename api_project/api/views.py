from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import BookSerializer
from .models import Book
# Create your views here.


class BookList(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
