from django.contrib import admin
from .models import Service, Interest, ClientInterest, Review

# Register your models here.
admin.site.register(Service)
admin.site.register(Interest)
admin.site.register(ClientInterest)
admin.site.register(Review)