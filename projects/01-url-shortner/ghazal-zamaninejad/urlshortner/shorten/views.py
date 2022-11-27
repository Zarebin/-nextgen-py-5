from rest_framework import generics, status
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from .models import *
from .serializer import TinySerializer
import random, string

# Create your views here.
class ToShortURLCreateAPIView(generics.CreateAPIView):
    queryset = Tiny.objects.all()
    serializer_class = TinySerializer

    def generate_random(self):        
        short_url_length = 6

        # Generate a random string with given length characters
        res = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for i in range(short_url_length))
        # Convert the url to string
        return str(res)

    def perform_create(self, serializer):
        short = self.generate_random()
        while(Tiny.objects.filter(short_url=short).exists()):
            short = self.generate_random

        long = self.request.POST['long_url']
        serializer.save(long_url=long, short_url=short)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        request_url = request.data['long_url']
        if Tiny.objects.filter(long_url=request_url).exists():
            instance = Tiny.objects.get(long_url=request_url)
            print("short is:", instance.short_url)
            
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ToLongURLRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Tiny.objects.all()
    serializer_class = TinySerializer

    def retrieve(self, request, *args, **kwargs):
        
        short_request = self.request.GET['q']
        instance = Tiny.objects.get(short_url=short_request)
        # increase click counts by one whenever user asked for the long url
        instance.click_count += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
