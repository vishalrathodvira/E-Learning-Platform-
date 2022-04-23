from distutils.command.upload import upload
import email
import fileinput
from click import option
from django.db import models
from django.db.models.signals import post_save
from pandas import options







# Create your models here.
class Header(models.Model):
    title = models.CharField(max_length=50)
    image = models.FileField(upload_to='profile_pics/',default='profile_pics/default.jpg')
    description = models.TextField()

class Feature_Product(models.Model):
    image = models.FileField(upload_to='profile_pics/',default='profile_pics/default.jpg')
    subimage1 = models.FileField(upload_to='profile_pics/',default='profile_pics/default.jpg')
    subimage2 = models.FileField(upload_to='profile_pics/',default='profile_pics/default.jpg')
    subimage3 = models.FileField(upload_to='profile_pics/',default='profile_pics/default.jpg')
    subimage4 = models.FileField(upload_to='profile_pics/',default='profile_pics/default.jpg')
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.CharField(max_length=100)
    mprice = models.CharField(max_length=100)
    def __str__(self):
        return self.name




class Address(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField(max_length=300)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    contry = models.CharField(max_length=100)
    zip = models.IntegerField()

class Payment(models.Model):
    cardname = models.CharField(max_length=100)
    crno = models.BigIntegerField()
    expmonth = models.IntegerField()
    expyear = models.IntegerField()
    cvv = models.IntegerField()
   

class Bestdeal(models.Model):
    name = models.CharField(max_length=50)
    image = image = models.FileField(upload_to='profile_pics/',default='profile_pics/default.jpg')
    description = models.CharField(max_length=100)
    description2 = models.CharField(max_length=100)



    
class New_Arrivals(models.Model):
    image = models.FileField(upload_to='profile_pics/',
    default='profile_pics/default.jpg')
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)

    mprice = models.CharField(max_length=50)
    def __str__(self):
        return self.name

    


class All_Product(models.Model):
    price = models.CharField(max_length=50)
    image = models.FileField(upload_to='profile_pics/',default='profile_pics/default.jpg')
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class feedback(models.Model):
    email=models.EmailField()
    def __str__(self):
        return self.email




   

 

