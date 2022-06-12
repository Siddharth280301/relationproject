from statistics import mode
from django.db import models

# Create your models here.
class Restaurant(models.Model):
    id = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=10)
    emp_restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)

