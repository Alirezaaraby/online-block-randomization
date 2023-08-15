from django.shortcuts import render, redirect
from home.models import patient, state
from home.forms import PatientForm
from django.http import HttpResponse
import csv


def index(request):
    data = patient.objects.all()
    if request.method == "POST":
        patient.objects.all().delete()
        state.objects.all().delete()
        return redirect("./")
    return render(request, "dashboard.html", {"data": data})


def edit(request, id):
    data = patient.objects.get(id=id)
    form = PatientForm(request.POST or None, instance=data)
    if form.is_valid():
        form.save()
        return redirect("view.patient")

    return render(request, "edit.html", {"data": data, "form": form})


def export_to_csv(request):
    patients = patient.objects.all()
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="file.csv"'
    writer = csv.writer(response)
    writer.writerow(
        ["name", "family name", "sex", "age", "code", "group", "registery time"]
    )
    patient_fields = patients.values_list(
        "name", "f_name", "sex", "age", "code", "group", "created_at"
    )
    for p in patients:
        writer.writerow([p.name, p.f_name, p.sex, p.age, p.code, p.group, p.created_at])
    return response
