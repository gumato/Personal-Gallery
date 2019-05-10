from django.db import models

# Create your models here.
class Location(models.Model):
    location=models.CharField(max_length=30)

    def __str__(self):
       return self.name


class Category(models.Model):
    name = models.CharField(max_length =100)

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.CharField(max_length =60)
    image_name = models.CharField(max_length =20)
    image_description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)




