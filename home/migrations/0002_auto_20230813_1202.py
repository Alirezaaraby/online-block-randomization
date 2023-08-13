# Generated by Django 3.2 on 2023-08-13 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='patient',
            name='code',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='patient',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sex',
            field=models.CharField(max_length=300),
        ),
    ]