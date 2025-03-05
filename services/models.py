from django.db import models
from accounts.models import Client, Freelancer

# Create your models here.

class Interest(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class clientInterests(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.interest

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    price = models.IntegerField()
    rating = models.FloatField(default=0)
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)
    delivery_time = models.IntegerField()
    
    def __str__(self):
        return self.title
    
class Review(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comment