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
            return render(request, 'pages/contact.html')
        else:
            context = {
                "errors": form.errors
            }

            return render(request, 'pages/contact.html', context)
