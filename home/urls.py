from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("patient/", views.patient, name="create.patient"),
]
