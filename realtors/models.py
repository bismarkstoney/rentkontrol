from django.db import models
from datetime import datetime
class Realtor(models.Model):
    name=models.CharField(max_length=150)
    photo=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    phone=models.CharField(max_length=50)
    email=models.CharField( max_length=50)
    decription=models.TextField(max_length=300)
    address=models.CharField(max_length=50)
    city=models.CharField( max_length=50)
    region=models.CharField(max_length=50)
    join_date=models.DateTimeField(default=datetime.now)
    is_mvp=models.DateTimeField(default=datetime.now)
    is_pop=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    


