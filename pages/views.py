from django.contrib import messages
from django.shortcuts import render

from pages.forms import ContactForm


def home_page_view(request):
    return render(request, 'index.html')


def about_page_view(request):
    return render(request, 'pages/about.html')


def contact_page_view(request):
    if request.method == "GET":
        return render(request, 'pages/contact.html')
    elif request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your contact information is sent to database')
            return render(request, 'pages/contact.html')
        else:
            messages.error(request, 'Something getting wrong, please try again later')
            return render(request, 'pages/contact.html')
