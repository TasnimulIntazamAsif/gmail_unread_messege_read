from django.db import models

class Email(models.Model):
    sender = models.CharField(max_length=255)
    subject = models.TextField()
    body = models.TextField()
    status = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    timestamp = models.CharField(max_length=50)