from django.db import models


class Author(models.Model):
    """
    Represents a book author.

    Fields:
        name (str): The full name of the author.
    """

    name = models.CharField(max_length=50)

    def __str__(self):
        """
        String representation of the Author object.
        Returns the author's name.
        """
        return self.name


class Book(models.Model):
    """
    Represents a book written by an author.

    Fields:
        title (str): The title of the book.
        publication_year (int): The year the book was published.
        author (Author): Foreign key relation to the Author model.
    """

    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )

    def __str__(self):
        """
        String representation of the Book object.
        Returns the book title.
        """
        return self.title
