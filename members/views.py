from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .decorators import superuser_required

# Create your views here.


@superuser_required
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {"form": form})


@login_required
def profile(request):
    context = request.user.is_superuser

    return render(request, "profile.html", {"is_superuser": context})
