from django.db import models

# Create your models here.
class Location(models.Model):
    location=models.CharField(max_length=30)

    def __str__(self):
       return self.location
    
    def save_locations(self):
        self.save()

    def delete_locations(self):
        self.delete()


class Category(models.Model):
    name = models.CharField(max_length =100)

    def __str__(self):
        return self.name
    

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Image(models.Model):
    image = models.ImageField(upload_to='photo/')
    image_name = models.CharField(max_length =20,blank=False)
    image_description = models.TextField(max_length=80,blank=False)
    location = models.ForeignKey(Location)
    category = models.ManyToManyField(Category)
    location = models.ForeignKey(Location)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.image_name
    class Meta:
        ordering = ["-comments_posts__timestamp","-comments_post__updated"]

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    @classmethod
    def get_all(cls):
        images = cls.objects.all()
        return images
    
    @classmethod
    def filter_category(cls,query):
        images = cls.objects.filter(category__name=query)
        return images

    @classmethod
    def search_by_category(cls, search_term):
        images = cls.objects.filter(category__name__icontains = search_term).order_by('-pub_date_posted')
        return images   



