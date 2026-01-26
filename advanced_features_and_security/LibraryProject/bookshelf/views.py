from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

# Create your views here.

@permission_required('bookshelf.can_add', raise_exception=True)
def edit_view(request):
    return render(request, 'bookshelf/edit.html')


def book_list_view(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})