from django.db import models


class patient(models.Model):
    name = models.CharField(max_length=300)
    f_name = models.CharField(max_length=300)
    sex = models.CharField(max_length=300)
    age = models.CharField(max_length=300)
    code = models.CharField(max_length=300)
    group = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)