from django.db import models
from accounts.models import Freelancer

# Create your models here.

class Services(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.name