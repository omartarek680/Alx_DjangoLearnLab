from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.ListView.as_view(), name="book-list"),
    path("books/create/", views.CreateView.as_view(), name="book-create"),
    path("books/<int:pk>/", views.DetailView.as_view(), name="book-detail"),
    path("books/delete/<int:pk>/", views.DeleteView.as_view(), name="book-delete"),
    path("books/update/<int:pk>/", views.UpdateView.as_view(), name="book-update"),
]
