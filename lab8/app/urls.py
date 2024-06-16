# lab8/app/urls.py

from django.urls import path
from .views import generate_pdf

urlpatterns = [
    path('generate_pdf/', generate_pdf, name='generate_pdf'),
]

