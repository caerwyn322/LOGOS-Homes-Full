from django.contrib import admin
from django.urls import path, include
from .views import GalleryView


urlpatterns = [
    path(r'', GalleryView.as_view(), name="Gallery")
]