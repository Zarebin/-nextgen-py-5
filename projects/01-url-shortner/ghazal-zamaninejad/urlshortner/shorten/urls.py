from django.urls import path
from .views import *

urlpatterns = [
    path('short/', TinyURLCreateAPIView.as_view()),
    path('long/', LongURLRetrieveAPIView.as_view())
]