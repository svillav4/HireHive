from django.db import models
from accounts.models import Client
from services.models import Service

# Create your models here.

class Order(models.Model):
    class Status(models.TextChoices):
        COMPLETED = 'Completed', 'Completed'
        CANCELLED = 'Cancelled', 'Cancelled'
        PENDING_APPROVAL = 'Pending Approval', 'Pending Approval'
        PENDING_PAYMENT = 'Pending Payment', 'Pending Payment'
        IN_PROGRESS = 'In Progress', 'In Progress'

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING_APPROVAL,
    )
    payment_method = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    
class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount = models.IntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)
    
    
