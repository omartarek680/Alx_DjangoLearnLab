from django.urls import path
from . import views

urlpatterns = [
    # Auth pages
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile_view, name="profile"),
    path("home/", views.home_view, name="home"),

    # Template-based posts CRUD
    path("posts/", views.PostListView.as_view(), name="posts-list"),
    path("posts/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("posts/new/", views.PostCreateView.as_view(), name="post-create"),
    path("posts/<int:pk>/edit/", views.PostUpdateView.as_view(), name="post-update"),
    path("posts/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post-delete"),

    # API endpoints (JSON)
    path("api/posts/", views.PostListAPI.as_view(), name="api-posts-list"),
    path("api/posts/<int:pk>/", views.PostDetailAPI.as_view(), name="api-post-detail"),
    path("api/posts/create/", views.PostCreateAPI.as_view(), name="api-post-create"),
    path("api/posts/<int:pk>/update/", views.PostUpdateAPI.as_view(), name="api-post-update"),
    path("api/posts/<int:pk>/delete/", views.PostDeleteAPI.as_view(), name="api-post-delete"),
]
