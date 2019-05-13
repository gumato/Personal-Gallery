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

    def test_delete_method(self):
        self.pricilla.save()
        self.pricilla.delete()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)

class CategoryTestClass(TestCase):

    def setUp(self):
        self.category= Category(name = 'sports')

    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))

    def test_save_method(self):
        self.category.save()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

class ImageTestClass(TestCase):

    def setUp(self):
        pricilla= Location(location = 'America')
        pricilla.save()
        self.image= Image(image = 'pricilla', image_name = 'image name', description = 'description', location = pricilla)
        
        # Creating a new tag and saving it image
        self.new_category = Category(name = 'testing')
        self.new_category.save()

        self.new_image= Image(image = 'Test Image',image_name = 'This is a random test Post', description = 'description',location = pricilla)
        self.new_image.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

    def test_save_method(self):
            self.image.save()
            images = Image.objects.all()
            self.assertTrue(len(images) > 0)