from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to='images', blank=True, null=True, default='default-avatar.jpg')
    is_freelancer = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
class Freelancer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.FloatField(default=0)
    portfolio = models.CharField(max_length=100, null=True, blank=True)
    experience = models.TextField()
    
    def __str__(self):
        return self.user.username
    
    