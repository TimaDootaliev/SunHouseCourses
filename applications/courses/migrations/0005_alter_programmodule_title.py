# Generated by Django 4.2.2 on 2023-07-07 08:25
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0004_addition_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="programmodule",
            name="title",
            field=models.CharField(max_length=150),
        ),
    ]
