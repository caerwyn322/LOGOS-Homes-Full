from django.contrib import admin
from django.urls import path, include
from .views import ContactView


urlpatterns = [
    path(r'', ContactView.as_view(), name="Contact-Us")
]