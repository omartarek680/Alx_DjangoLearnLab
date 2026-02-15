from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomCreationForm


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
    pass

def logout_view(request):
    pass

def profile_view(request):
    pass

def home_view(request):
    pass

def posts_view(request):
    pass