from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("patient/", views.patient_handler, name="create.patient"),
]
