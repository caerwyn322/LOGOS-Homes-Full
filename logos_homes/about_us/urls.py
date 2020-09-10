from django.contrib import admin
from django.urls import path, include
from .views import AboutUsView


urlpatterns = [
    path(r'', AboutUsView.as_view(), name="About0Us")
]