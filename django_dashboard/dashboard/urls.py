from django.urls import path
from .views import email_list

urlpatterns = [
    path('', email_list),
]