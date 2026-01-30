from django.shortcuts import render
from  rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from .serializers import BookSerializer
from .models import Book
from  rest_framework import viewsets
# Create your views here.


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
