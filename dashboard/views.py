from django.shortcuts import render, redirect
from home.models import patient
from home.forms import PatientForm


def index(request):
    data = patient.objects.all()
    return render(request, "dashboard.html", {"data": data})


def edit(request, id):
    data = patient.objects.get(id=id)
    form = PatientForm(request.POST or None, instance=data)
    if form.is_valid():
        form.save()
        return redirect("view.patient")

    return render(request, "edit.html", {"data": data, "form": form})
