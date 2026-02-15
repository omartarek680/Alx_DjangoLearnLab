from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomCreationForm, PostForm
from django.contrib.auth import login, logout, authenticate
from rest_framework import generics
from .serializers import PostSerializer
from .models import Post
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import FormView
# Create your views here.

class RegisterView(CreateView):
    model = Post
    form_class = CustomCreationForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')

class LoginView(FormView):
    template_name = 'blog/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('profile')
    def form_valid(self,form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)


def logout_view(request):
    pass

def profile_view(request):
    pass

def home_view(request):
    pass
@login_required
def posts_view(request):
    posts = Post.objects.filter(author=request.user)
    return render(request,'blog/all-posts.html',{'post':posts})

def post_detail_view(request,pk):
    post = Post.objects.filter(pk=pk)
    return render(request,'blog/post-detail.html',{'post':post})

class ListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
