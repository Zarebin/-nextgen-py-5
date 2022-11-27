from django.urls import path
from .views import *

urlpatterns = [
    path('to-short/', ToShortURLCreateAPIView.as_view()),
    path('to-long/', ToLongURLRetrieveAPIView.as_view())
]