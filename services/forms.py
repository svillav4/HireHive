from django import forms
from .models import Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            'title', 'description', 'image', 'price', 'category', 'delivery_time' 
        ] 