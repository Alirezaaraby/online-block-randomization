from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PatientForm
from random import randint


def index(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'patients.html', {})

