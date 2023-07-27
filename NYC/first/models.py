from django.db import models

# Create your models here.
class FeedbackForm(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.CharField(max_length=500)




class Cars(models.Model):
    Brand = models.CharField(max_length=20)
    Model = models.CharField(max_length=20)
    Color = models.CharField(max_length=20)
    Price = models.CharField(max_length=500)
    #Img = models.ImageField()
   



class Music(models.Model):
    Artist = models.CharField(max_length=200)
    Album = models.CharField(max_length=200)
    Year = models.CharField(max_length=200)
    Price = models.CharField(max_length=500)
   





