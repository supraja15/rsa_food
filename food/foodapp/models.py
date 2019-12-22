from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here .

class SouthIndianFood(models.Model):
    name=models.CharField(max_length=200,primary_key=True)
    price=models.PositiveIntegerField()
    def __str__(self):
        return self.name
class NorthIndiaFood(models.Model):
    name=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    def __str__(self):
        return self.name
class ChineseFood(models.Model):
    name=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    def __str__(self):
        return self.name
