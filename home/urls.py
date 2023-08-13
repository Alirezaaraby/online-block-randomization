from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="create.patient"),
    # path("create/", views.index),
]
