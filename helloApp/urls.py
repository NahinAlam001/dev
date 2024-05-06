# api/urls.py
from django.urls import path, include

urlpatterns = [
    path('', include('example.urls')),
]
