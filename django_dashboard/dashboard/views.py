from django.shortcuts import render
from .models import Email

def email_page(request):
    emails = Email.objects.all().order_by('-id')
    return render(request,"emails.html",{"emails":emails})