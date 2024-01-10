from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    profile_picture = models.ImageField(upload_to='profile_pic/', default='default_profile.jpg')
    occupation = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Finance(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='finances')    
    category = models.CharField(max_length=50, blank=False, null=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    income = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return self.category
