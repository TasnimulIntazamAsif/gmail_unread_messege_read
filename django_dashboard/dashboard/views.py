from django.shortcuts import render
from .models import Email

def email_list(request):
    query = request.GET.get('q')
    status = request.GET.get('status')
    category = request.GET.get('category')

    emails = Email.objects.all()

    if query:
        emails = emails.filter(subject__icontains=query) | emails.filter(sender__icontains=query)

    if status:
        emails = emails.filter(status=status)

    if category:
        emails = emails.filter(category=category)

    return render(request, "emails.html", {"emails": emails})