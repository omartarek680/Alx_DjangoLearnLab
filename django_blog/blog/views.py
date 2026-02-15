from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomCreationForm
from django.contrib.auth import login, logout, authenticate
from rest_framework import generics
from .serializers import PostSerializer
from .models import Post
# Create your views here.


def reqgister_view(request):
    if request.method == 'POST':
        form = CustomCreationForm(request.data)

        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        form = UserCreationForm()

    return render(request, 'blog/register.html',{'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.data)
        
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('profile')
        
    else:
        form = AuthenticationForm()

    return render(request,'blog/login.html',{'form':form})    

def logout_view(request):
    pass

def profile_view(request):
    pass

def home_view(request):
    pass

# def posts_view(request):
#     pass


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
