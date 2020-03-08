from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http.response import HttpResponse

from account.forms import RegistrationForm


def registrationView(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.isValid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)

