from django.db import models
from datetime import datetime


class Contacts(models.Model):
    listing=models.CharField(max_length=250)
    listing_id=models.IntegerField()
    name=models.CharField(max_length=200)
    email=models.CharField( max_length=50)
    phone=models.CharField(max_length=50)
    location=models.CharField( max_length=250)
    message=models.TextField(blank=True)
    user_id=models.IntegerField(blank=True)
    contact_date= models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self):
        return self.name
    
    
