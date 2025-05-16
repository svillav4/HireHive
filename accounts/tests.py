from django.test import TestCase
from accounts.models import User, Freelancer, Client

# Create your tests here.
class FreelancerModelTest(TestCase):
    def test_create_freelancer_user(self):
        user = User.objects.create_user(username='freelancer1', password='test1234', is_freelancer=True)
        freelancer = Freelancer.objects.create(user=user, experience='5 years of experience in web design')
        self.assertEqual(freelancer.user.username, 'freelancer1')

class ClientModelTest(TestCase):
    def test_create_client_user(self):
        user = User.objects.create_user(username='client1', password='test1234')
        client = Client.objects.create(user=user)
        self.assertEqual(client.user.username, 'client1')