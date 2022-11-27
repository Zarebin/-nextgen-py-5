from rest_framework import serializers
from .models import *

class TinySerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField('get_shorten')

    def get_shorten(self, id):
        short = Tiny.objects.get(short_url=id.short_url).short_url
        short = 'myshortner.ir/' + short
        return short

    class Meta:
        model = Tiny
        fields = '__all__'