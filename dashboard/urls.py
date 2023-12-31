from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="view.patient"),
    path("edit/<int:id>", views.edit, name="edit.patient"),
    path("export_to_csv/", views.export_to_csv, name="csv.patient"),
]
