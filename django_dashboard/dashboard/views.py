from django.shortcuts import render
from .models import Email
from django.db.models import Q

def email_page(request):
    emails = Email.objects.all().order_by('-id')

    q = request.GET.get("q")
    status = request.GET.get("status")
    category = request.GET.get("category")

    if q:
        emails = emails.filter(
            Q(subject__icontains=q) |
            Q(sender__icontains=q) |
            Q(body__icontains=q)
        )

    if status:
        emails = emails.filter(status=status)

    if category:
        emails = emails.filter(category=category)

    return render(request,"emails.html",{"emails":emails})