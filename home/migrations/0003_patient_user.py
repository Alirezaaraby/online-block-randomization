# Generated by Django 4.2.3 on 2023-08-15 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_state_alter_patient_age_alter_patient_code_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="patient",
            name="user",
            field=models.CharField(default="admin", max_length=300),
        ),
    ]
