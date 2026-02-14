from rest_framework import serializers
from .models import Author, Book
from datetime import date


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.

    Fields:
        - id: Auto-generated primary key.
        - title: Title of the book.
        - publication_year: Year the book was published.
        - author: Foreign key reference to Author.

    Validation:
        - publication_year cannot be in the future.
    """

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, val):
        """
        Ensure publication_year is not greater than the current year.
        """
        current_year = date.today().year

        if val > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )

        return val


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True,source="books")

    class Meta:
        model = Author
        fields = ["id", "name", "books"]