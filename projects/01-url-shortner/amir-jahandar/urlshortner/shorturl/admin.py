from django.contrib import admin
from .models import ShortUrl, Profile


admin.site.register(ShortUrl)
admin.site.register(Profile)
