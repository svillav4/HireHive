from django.db import models
from accounts.models import Client
from services.models import Service

# Create your models here.

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    
class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount = models.IntegerField()
    status = models.BooleanField(default=False)
    
    
