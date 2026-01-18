from relationship_app.models import Author, Book, Library, Librarian
author_name = Author.objects.get(name='Omar')
books = Book.objects.filter(author=author_name)
library_name = "Alex"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
library_name = Library.objects.get(name='library_name')
librarian = Librarian.objects.get(library=library_name)
print(librarian.name)