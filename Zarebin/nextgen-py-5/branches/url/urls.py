from django.urls import path
from . import views
from .models import UrlData

app_name = "url"
urlpatterns = [
    path("", views.index, name="home"),
    path("u/<str:slugs>", views.urlRedirect, name="redirect"),
    path("", views.urlShort, name = "Short"),
    path("", UrlData)

]
