from django.urls import path
from . import views

urlpatterns = [
    # This leaves the path empty so it combines with the project path
    # Result: /books/ + '' = /books/
    path('', views.list_books, name='list_books'),
]