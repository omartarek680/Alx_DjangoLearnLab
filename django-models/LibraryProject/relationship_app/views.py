# relationship_app/views.py
from django.shortcuts import redirect, render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class ListBooksView(ListView):
    model = Book
    template_name = 'relationship_app/list_books.html'
    context_object_name = 'books'

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'relationship_app/register.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'relationship_app/register.html', {'form': form})


# def is_admin(user):
#         if user.is_authenticated and user.userprofile.role == 'Admin':
#             return True
#         raise PermissionDenied

def is_librarian(user):
    if user.is_authenticated and user.userprofile.role == 'Librarian':
        return True
    raise PermissionDenied

def is_member(user):
    if user.is_authenticated and user.userprofile.role == 'Member':
        return True
    raise PermissionDenied
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


# @login_required
# @user_passes_test(is_admin)
# def admin_view(request):
#     return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')