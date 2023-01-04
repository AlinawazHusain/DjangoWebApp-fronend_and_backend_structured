from django.db import models
from datetime import datetime

class Data(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=12)
    email=models.EmailField(max_length=50)
    order=models.CharField(max_length=100)
    date=models.DateField()

    def __str__(self):
        return self.name
