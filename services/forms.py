from django import forms
from .models import Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            'title', 'description', 'image', 'price', 'interest', 'delivery_time' 
        ] 