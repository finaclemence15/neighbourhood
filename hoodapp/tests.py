from django.test import TestCase
from . models import Comment, Business, Post,Neighbourhood, Profile

# Create your tests here.


# Create your tests here.

class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User.objects.create_user(username='thoni', password='qwertyuiop')
        self.profile = Profile(id=1, name='Tom Thomassen',user = self.user,bio='Bionic')
    # Test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))


