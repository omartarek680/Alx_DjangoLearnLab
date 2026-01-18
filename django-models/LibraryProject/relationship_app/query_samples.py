from relationship_app.models import Author, Book, Library, Librarian
omar = Author.objects.get(name='Omar')
books = Book.objects.filter(author=omar)
for book in books:
    print(book.title)


library = Library.objects.get(name='library_name')
books = library.books.all()
for book in books:
    print(book.title)

library = Library.objects.get(name='library_name')
librarian = Librarian.objects.get(library=library)
print(librarian.name)