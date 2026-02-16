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