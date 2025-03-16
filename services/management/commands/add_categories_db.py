from django.core.management.base import BaseCommand
from services.models import Category
import json

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        json_file_path = 'services/management/commands/categories.json'

        with open(json_file_path, 'r') as file:
            categories = json.load(file)
        
        for i in range(len(categories)):
            category = categories[i]
            exist = Category.objects.filter(name=category['name']).first()
            if not exist:
                Category.objects.create(name=category['name'])
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded categories from categories.json'))