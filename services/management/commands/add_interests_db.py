from django.core.management.base import BaseCommand
from services.models import Interest
import json

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        json_file_path = 'services/management/commands/interests.json'

        with open(json_file_path, 'r') as file:
            interests = json.load(file)
        
        for i in range(len(interests)):
            interest = interests[i]
            exist = Interest.objects.filter(name=interest['name']).first()
            if not exist:
                Interest.objects.create(name=interest['name'])
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded interests from interests.json'))