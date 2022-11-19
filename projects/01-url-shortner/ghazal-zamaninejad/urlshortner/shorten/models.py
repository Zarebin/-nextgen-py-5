from pyexpat import model
from django.db import models

# Create your models here.
class Tiny(models.Model):
    long_url = models.TextField()
    short_url = models.CharField(max_length=20, blank=True, null=True)
# class Number(models.Model):
#     s = models.CharField(max_length=200)
#     number_int = models.IntegerField(blank=True, null=True)