from django.db import models
import datetime as dt


# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    occupants_count = models.IntegerField()   
    Admin = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    country = CountryField(blank_label='(select country)', default='NG')
