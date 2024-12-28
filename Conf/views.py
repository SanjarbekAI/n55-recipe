from django.shortcuts import render


def custom_handler404(request, exception):
    return render(request, 'pages/404.html')
