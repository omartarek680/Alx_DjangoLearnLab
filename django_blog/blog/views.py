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
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
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

@login_required
def logout_view(request):
    logout(request)
    return redirect("login")

class ListPosts(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/all-posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).order_by('-published_date')

class DetailPost(LoginRequiredMixin,DetailView):
    model = Post
    template_name = 'blog/post-detail.html'
    context_object_name = 'post'
    def get_queryset(self):

 
       return Post.objects.filter(author= self.request.user)



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
