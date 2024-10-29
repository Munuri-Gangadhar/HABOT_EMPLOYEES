from django.db import models
from datetime import date
# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    department=models.CharField(max_length=50,blank=True)
    role=models.CharField(max_length=50,blank=True)
    date_joined=models.DateField(default=date.today)

    def __str__(self):
        return self.name
