from django.db import models

# Create your models here.


    # <!-- fashion section start -->
class Fashion(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.name
        # Man T -shirt
        # Man -shirt
        # Woman Scart
    # <!-- fashion section end -->



    # <!-- electronic section start -->
class Electronic(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.name
        # Laptop
        # Mobile
        # Computers
    # <!-- electronic section end -->


    # <!-- jewellery  section start -->
class Jewellery(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.name
        # Jumkas
        # Necklaces
        # Kangans
    # <!-- jewellery  section end -->


    # Price
    # images