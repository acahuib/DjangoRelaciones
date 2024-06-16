# lab8/app/urls.py

from django.urls import path
from .views import generate_pdf, send_test_email

urlpatterns = [
    path('generate_pdf/', generate_pdf, name='generate_pdf'),
    path('send_test_email/', send_test_email, name='send_test_email'),
]

