from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("patient/", views.patient_handler, name="create.patient"),
]
