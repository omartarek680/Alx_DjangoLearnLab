from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import FormView

from .models import Post
from .forms import CustomCreationForm, PostForm

# DRF
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import PostSerializer


User = get_user_model()

# ---------------------------
# Auth (Templates)
# ---------------------------

class RegisterView(CreateView):
    model = User                 # ✅ User, not Post
    form_class = CustomCreationForm
    template_name = "blog/register.html"
    success_url = reverse_lazy("login")


class LoginView(FormView):
    template_name = "blog/login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


@login_required
def logout_view(request):
    logout(request)
    return redirect("login")


def profile_view(request):
    # TODO: render profile template if you have one
    return render(request, "blog/profile.html")


def home_view(request):
    return render(request, "blog/home.html")


# ---------------------------
# Posts CRUD (Templates)
# templates expected:
# - blog/all-posts.html
# - blog/post-detail.html
# - blog/post_form.html
# - blog/post_confirm_delete.html
# ---------------------------

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "blog/all-posts.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).order_by("-published_date")


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "blog/post-detail.html"
    context_object_name = "post"

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("posts-list")

    def form_valid(self, form):
        form.instance.author = self.request.user  # ✅ user can’t fake author
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("posts-list")

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("posts-list")

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


# ---------------------------
# Posts API (DRF)
# Prefix them with /api/
# ---------------------------

class PostListAPI(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).order_by("-published_date")


class PostDetailAPI(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


class PostCreateAPI(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostUpdateAPI(generics.UpdateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


class PostDeleteAPI(generics.DestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
