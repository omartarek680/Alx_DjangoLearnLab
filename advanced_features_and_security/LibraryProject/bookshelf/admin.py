from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Book, CustomUser
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author','publication_year')
    list_filter = ('publication_year',)

@admin.register(CustomUser,UserAdmin)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'date_of_birth', 'favorite_genre')
    search_fields = ('username', 'email')
    list_filter = ('date_of_birth',)