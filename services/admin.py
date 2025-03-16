from django.contrib import admin
from .models import Service, Category, Review

# Register your models here.
admin.site.register(Service)
admin.site.register(Category)
admin.site.register(Review)