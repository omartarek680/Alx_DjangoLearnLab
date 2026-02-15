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
    path('post/new/', views.CreateView.as_view(), name='create-post'),
    path('post/<int:pk>/update/', views.UpdateView.as_view(), name='update-post'),
    path('post/<int:pk>/delete/', views.DetailView.as_view(), name='delete-post'),

]