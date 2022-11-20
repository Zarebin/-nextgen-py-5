from django.contrib import admin
from django.urls import path, include

from .views import home, createshorturl, redirect_url, signup, login, logout

urlpatterns = [
    path('', home , name= 'home'),
    path('signup/', signup, name='signup' ),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('create/', createshorturl, name = 'create'),
    path('<str:url>/', redirect_url, name= 'redirect'),
    path('admin/', admin.site.urls),
]
