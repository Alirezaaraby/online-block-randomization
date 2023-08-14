from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PatientForm
from random import randint
from .models import state, patient

state = [
    ["A", "A", "B", "B"],
    ["B", "B", "A", "A"],
    ["A", "B", "A", "B"],
    ["B", "A", "B", "A"],
    ["A", "B", "B", "A"],
    ["B", "A", "A", "B"],
]


def index(request):
    return render(request, "index.html")


def patient_handler(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            last_id = patient.objects.count()

            if last_id % 4 == 0:
                random_state = state[randint(0, 5)]
                state.objects.create(
                    first=random_state[0],
                    second=random_state[1],
                    third=random_state[2],
                    fourth=random_state[3],
                )
                name = request.POST.get("name")
                f_name = request.POST.get("f_name")
                sex = request.POST.get("sex")
                age = int(request.POST.get("age"))
                code = int(request.POST.get("code"))

                person = patient.objects.create(
                    name=name,
                    f_name=f_name,
                    sex=sex,
                    age=age,
                    code=code,
                    group=random_state[0],
                )

                return HttpResponse(random_state[0])
            else:
                if last_id % 4 == 1:
                    pass
                elif last_id % 4 == 2:
                    pass
                elif last_id % 4 == 3:
                    pass
                
    return render(request, "patients.html", {})
