from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomCreationForm
from django.contrib.auth import login, logout, authenticate


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
        form = AuthenticationForm(request.data)
        if form.is_valid():
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

def posts_view(request):
    pass