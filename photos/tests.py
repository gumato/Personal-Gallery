from django.test import TestCase
from .models import Location, Category, Image



# Create your tests here.

class LocationTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.pricilla= Location(location = 'America')

    def test_instance(self):
        self.assertTrue(isinstance(self.pricilla,Location))

    def test_save_method(self):
        self.pricilla.save()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)
 