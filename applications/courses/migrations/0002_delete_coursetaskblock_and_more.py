# Generated by Django 4.2.2 on 2023-07-05 08:57
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="CourseTaskBlock",
        ),
        migrations.RenameField(
            model_name="course",
            old_name="is_banned",
            new_name="is_published",
        ),
        migrations.DeleteModel(
            name="TestAnswer",
        ),
        migrations.DeleteModel(
            name="TestQuestion",
        ),
    ]
