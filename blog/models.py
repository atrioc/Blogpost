from django.db import models
from django.forms import CharField
from datetime import datetime

# Create your models here.

class posts(models.Model):
    title =models.CharField(max_length=50)
    data =models.CharField(max_length=100000)
    date =models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.title
