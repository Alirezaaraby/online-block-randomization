from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PatientForm
from random import randint
from .models import state, patient
from django.contrib.auth.decorators import login_required

state_list = [
    ["A", "A", "B", "B"],
    ["B", "B", "A", "A"],
    ["A", "B", "A", "B"],
    ["B", "A", "B", "A"],
    ["A", "B", "B", "A"],
    ["B", "A", "A", "B"],
]


def index(request):
    return render(request, "index.html")


@login_required
def patient_handler(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            last_id = patient.objects.count()
            username = request.user.username
            if last_id % 4 == 0:
                random_state = state_list[randint(0, 5)]
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
                    user=username,
                )
                if random_state[0] == "A":
                    return render(request, "a.html")
                elif random_state[0] == "B":
                    return render(request, "b.html")
            else:
                latest_state = state.objects.latest("id")

                if last_id % 4 == 1:
                    group = latest_state.second
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
                        group=group,
                        user=username,
                    )
                    if group == "A":
                        return render(request, "a.html")
                    elif group == "B":
                        return render(request, "b.html")
                elif last_id % 4 == 2:
                    group = latest_state.third
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
                        group=group,
                        user=username,
                    )
                    if group == "A":
                        return render(request, "a.html")
                    elif group == "B":
                        return render(request, "b.html")
                elif last_id % 4 == 3:
                    group = latest_state.fourth
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
                        group=group,
                        user=username,
                    )
                    if group == "A":
                        return render(request, "a.html")
                    elif group == "B":
                        return render(request, "b.html")

    return render(request, "patients.html", {})
