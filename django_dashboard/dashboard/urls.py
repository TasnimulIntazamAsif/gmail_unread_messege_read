from django.urls import path
from .views import email_page

urlpatterns = [
    path('', email_page),
]