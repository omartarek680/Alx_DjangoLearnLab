from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.reqgister_view, name='register'),
    path('login/',views.login_view, name='login'),
    path('logout',views.logout_view, name='logout'),
    path('profile/',views.profile_view, name= 'profile'),
    path('home/',views.home_view, name= 'home'),
    path('posts/', views.ListView.as_view(), name='posts'),
    path('posts/<int:pk>/', views.DetailView.as_view(), name='detail-post'),
    path('posts/new/', views.CreateView.as_view(), name='create-post'),
    path('posts/<int:pk>/edit/', views.UpdateView.as_view(), name='edit-post'),
    path('posts/<int:pk>/delete/', views.DetailView.as_view(), name='delete-post'),

]