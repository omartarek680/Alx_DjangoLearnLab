from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUserModel(AbstractUser):
	bio = models.TextField()
	profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
	followers = models.ManyToManyField(
		'self',
		symmetrical=False,
		related_name="following",          # reverse name
        related_query_name="following", 
    )


class Post(models.Model):
	author = models.ForeignKey(CustomUserModel,on_delete=models.CASCADE, related_name='authored_posts')
	title = models.CharField(max_length=100)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	author = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='comments')
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)