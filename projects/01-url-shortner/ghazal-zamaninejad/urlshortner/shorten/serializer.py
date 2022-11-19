from rest_framework import serializers
from .models import *

class TinySerializer(serializers.ModelSerializer):
    class Meta:
        model = Tiny
        fields = '__all__'