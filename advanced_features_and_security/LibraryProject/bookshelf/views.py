from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm
# Create your views here.

@permission_required('bookshelf.can_add', raise_exception=True)
def edit_view(request):
    return render(request, 'bookshelf/edit.html')


def book_list_view(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})



def form_example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            return render(request, 'bookshelf/form_success.html', {'name': name, 'email': email})
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})