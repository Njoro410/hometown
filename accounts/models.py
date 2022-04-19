from django.db import models
from django.contrib.auth.models import User
import geocoder

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to = 'profile/', default='Profile_pic')
    location = models.ForeignKey('Neighbourhood', on_delete=models.CASCADE, null=True)
    
    
    def __str__(self):
        return f'{self.user}'
    
 
access_key = 'pk.eyJ1Ijoibmpvcm80MTAiLCJhIjoiY2wyM3VpMTVqMGYwMzNkcDk5NnB2ZHliNiJ9.GqXYjw7RS2cGhtzAiPt0Nw'
   
class Neighbourhood(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)
   
    
    
    def __str__(self):
        return self.address
    
    def save(self,*args, **kwargs):
        g = geocoder.mapbox(self.address, key = access_key)
        g = g.latlng
        self.lat = g[0]
        self.long = g[1]
        return super(Neighbourhood, self).save(*args, **kwargs)
    

    