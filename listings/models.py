from django.db import models
from django.urls import reverse
from datetime import datetime

import uuid
from .choices import yes_no, conditions, property_types
from realtors.models import Realtor
class Listing(models.Model):
    slug=models.UUIDField(default=uuid.uuid4, editable=False)
    realtor=models.ForeignKey(Realtor, on_delete=models.CASCADE)
    title = models.CharField(max_length = 250)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    region=models.CharField(max_length=250)
    description= models.TextField(blank=True)
    price=models.IntegerField()
    somking=models.CharField(max_length=50, choices=yes_no)
    selfmeter=models.CharField(max_length=50, choices=yes_no)
    polythank=models.CharField(max_length=50, choices=yes_no)
    lanlord=models.CharField(max_length=50, choices=yes_no)
    parking=models.CharField(max_length=50, choices=yes_no)
    pets=models.CharField(max_length=50, choices=yes_no)
    closedtoroad=models.CharField(max_length=50, choices=yes_no)
    condition=models.CharField(max_length=50, choices=conditions)
    propertytype=models.CharField(max_length=50, choices=property_types)
    bedrooms=models.IntegerField()
    bathromms=models.IntegerField()
    garage=models.IntegerField(default=0)
    sqft=models.IntegerField()
    lot_size=models.DecimalField(max_digits=5, decimal_places=2)
    photo_main=models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_2=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_3=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_4=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_5=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_6=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    is_published=models.BooleanField(default=True)
    list_date=models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('listing', args=[str(self.slug)])   
    

    
