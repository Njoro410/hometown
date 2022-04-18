from django.forms import EmailField
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from accounts.models import Address

# Create your models here.
class Business(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    location = models.ForeignKey(Address, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Hospitals(models.Model):
    name = models.CharField(max_length=50)
    # location = models.CharField(max_length=50)
    phone = PhoneNumberField( region='KE')
    email = models.EmailField()
    location = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Police(models.Model):
    station = models.CharField(max_length=50)
    # location = models.CharField(max_length=50)
    phone = PhoneNumberField( region='KE')
    email = models.EmailField()
    location = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.station
    
class Posts(models.Model):
    posted_on = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    content = models.TextField()
    location = models.ForeignKey(Address, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tags')
    
    def __str__(self):
        return self.title
    
class Tags(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
