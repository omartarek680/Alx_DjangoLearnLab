from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.reqgister_view, name='register'),
    path('login/',views.login_view, name='login'),
    path('logout',views.logout_view, name='logout'),
    path('profile/',views.profile_view, name= 'profile'),
    path('home/',views.home_view, name= 'home'),
    path('post/', views.posts_view, name= 'posts')
]