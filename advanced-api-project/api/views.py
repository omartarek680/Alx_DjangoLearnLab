from django.shortcuts import render
from rest_framework import generics
from .models import Author, Book
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class ListView(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        qs = Book.objects.select_related("author").all()

        title = self.request.query_params.get("title")
        year = self.request.query_params.get("publication_year")
        author_id = self.request.query_params.get("author_id")

        if title:
            qs = qs.filter(title__icontains=title)

        if year and year.isdigit():
            qs = qs.filter(publication_year=int(year))

        if author_id and author_id.isdigit():
            qs = qs.filter(author_id=int(author_id))

        return qs
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer  
    permission_classes = [IsAuthenticated] 