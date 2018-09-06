from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    company = models.CharField(max_length=100, blank=True)
    school = models.CharField(max_length=150, blank=True)
    college = models.CharField(max_length=150, blank=True)
    image = models.ImageField(upload_to='user_image',blank=True)

    def __str__(self):
        return self.user.username
