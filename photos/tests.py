from django.test import TestCase
from .models import Location,Category,Image

# Create your tests here.
class Location TestClass(TestCase):
    # Set up method
    def setUp(self):
        self.priclla= Location(location = 'America')
 # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.pricilla,Location))       

        
