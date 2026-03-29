from django.db import models


class Email(models.Model):

    sender = models.CharField(max_length=200)
    subject = models.CharField(max_length=500)
    time = models.CharField(max_length=100)

    def __str__(self):
        return self.subject