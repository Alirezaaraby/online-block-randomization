from django.db import models


class patient(models.Model):
    name = models.CharField(max_length=50)
    f_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1)
    age = models.IntegerField()
    code = models.IntegerField()
    group = models.CharField(max_length=1, null=False)
    user = models.CharField(max_length=300, default="admin", null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class state(models.Model):
    first = models.CharField(max_length=1)
    second = models.CharField(max_length=1)
    third = models.CharField(max_length=1)
    fourth = models.CharField(max_length=1)
