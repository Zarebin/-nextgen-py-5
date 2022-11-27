from pyexpat import model
from django.db import models

# Create your models here.
class Tiny(models.Model):
    long_url = models.TextField()
    short_url = models.CharField(max_length=20, blank=True, null=True)
    click_count = models.IntegerField(blank=True, default=0)