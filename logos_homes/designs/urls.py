from django.contrib import admin
from django.urls import path, include
from .views import DesignView


urlpatterns = [
    path(r'', DesignView.as_view(), name="Designs")
]