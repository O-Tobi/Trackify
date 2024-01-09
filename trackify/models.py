from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=False, null=False, unique=True)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    profile_picture = models.ImageField(upload_to='profile_pic/', default='default_profile.jpg')
    occupation = models.CharField(max_length=50, blank=False)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username

class Finance(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='finances')    
    category = models.CharField(max_length=50, blank=False, null=False)
    amount = models.IntegerField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    income = models.IntegerField(default=0)
    
    def __str__(self):
        return self.category
 


