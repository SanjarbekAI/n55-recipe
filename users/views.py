import threading

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.tokens import default_token_generator
from django.db.models import Q
from django.shortcuts import render, redirect

from users.forms import RegisterForm, LoginForm
from users.models import CustomUserModel
from users.utils import send_email_confirmation


def register_view(request):
    if request.method == "GET":
        return render(request, 'auth/register.html')
    elif request.method == "POST":
        data = request.POST
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.set_password(raw_password=data['password1'])
            user.save()

            email_thread = threading.Thread(target=send_email_confirmation, args=(user, request,))
            email_thread.start()

            messages.success(request, "Please, confirm your email and login")
            return redirect('users:login')
        else:
            messages.error(request, form.error_messages)
            return render(request, 'auth/register.html')


def confirm_email(request, uid, token):
    try:
        user = CustomUserModel.objects.get(id=uid)
    except CustomUserModel.DoesNotExist:
        return redirect('users:login')

    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Your email address is verified!")
        return redirect('users:login')
    else:
        messages.success(request, "Link is not correct")
        return redirect('users:login')


def login_view(request):
    if request.method == "GET":
        return render(request, 'auth/login.html')
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email_or_username = request.POST['email_or_username']
            password = request.POST['password']

            try:
                user = CustomUserModel.objects.get(
                    Q(username=email_or_username) | Q(email=email_or_username)
                )
            except CustomUserModel.DoesNotExist:
                return redirect('users:login')

            authenticated_user = authenticate(username=user.username, password=password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect('pages:home')
            else:
                return redirect('users:login')
        else:
            return redirect('users:login')
