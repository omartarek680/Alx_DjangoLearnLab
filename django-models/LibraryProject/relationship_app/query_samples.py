from relationship_app.models import Author, Book, Library, Librarian
authoe_name = Author.objects.get(name='author_name')
books = Book.objects.filter(author=authoe_name)
for book in books:
    print(book.title)
library_name = "Alex"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
library_name = Library.objects.get(name='library_name')
librarian = Librarian.objects.get(library=library_name)
print(librarian.name)