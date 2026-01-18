from relationship_app.models import Author, Book, Library, Librarian
omar = Author.objects.get(name='author_name')
books = Book.objects.filter(author=omar)
for book in books:
    print(book.title)

books = Book.objects.filter(libraries__name='library_name')
for book in books:
    print(book.title)
library = Library.objects.get(name='library_name')
librarian = Librarian.objects.get(library=library)
print(librarian.name)