from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=50, blank=False)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    profile_picture = models.ImageField(upload_to='profile_pic/', default='default_profile.jpg')
    occupation = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.username

class Finance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='finances')
    category = models.CharField(max_length=50, blank=False, null=False)
    amount = models.IntegerField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.category
