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
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {
            "fields": ("date_of_birth", "profile_photo"),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {
            "fields": ("date_of_birth", "profile_photo"),
        }),
    )
