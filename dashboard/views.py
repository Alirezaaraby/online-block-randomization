from django.shortcuts import render, redirect
from home.models import patient, state
from home.forms import PatientForm
from django.http import HttpResponse
import csv
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    context = request.user.is_superuser
    data = patient.objects.all()
    if request.method == "POST":
        patient.objects.all().delete()
        state.objects.all().delete()
        return redirect("./")
    return render(request, "dashboard.html", {"data": data, "is_superuser": context})


@login_required
def edit(request, id):
    data = patient.objects.get(id=id)
    form = PatientForm(request.POST or None, instance=data)
    if form.is_valid():
        form.save()
        return redirect("view.patient")

    return render(request, "edit.html", {"data": data, "form": form})


@login_required
def export_to_csv(request):
    patients = patient.objects.all()
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="file.csv"'
    writer = csv.writer(response)
    writer.writerow(
        [
            "name",
            "family name",
            "sex",
            "age",
            "code",
            "group",
            "nurse",
            "registery time",
        ]
    )
    patient_fields = patients.values_list(
        "name", "f_name", "sex", "age", "code", "group", "user", "created_at"
    )
    for p in patients:
        writer.writerow([p.name, p.f_name, p.sex, p.age, p.code, p.group, p.created_at])
    return response
