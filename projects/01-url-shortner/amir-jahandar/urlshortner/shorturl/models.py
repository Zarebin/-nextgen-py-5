from email.policy import default
from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    country = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.user


class ShortUrl(models.Model):
    original_url = models.URLField(max_length = 800)
    short_url = models.CharField(max_length = 50)
    time_date_created = models.DateTimeField()
    profile = models.ForeignKey(Profile, related_name = 'profile' ,on_delete= models.CASCADE, default=1)


    def __str__(self) -> str:
        return  f"{ self.original_url }"

