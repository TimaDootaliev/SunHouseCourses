# Generated by Django 4.2.2 on 2023-06-27 09:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="userprofile",
            options={
                "verbose_name": "User Profile",
                "verbose_name_plural": "User Profiles",
            },
        ),
        migrations.AlterField(
            model_name="user",
            name="is_teacher",
            field=models.BooleanField(
                default=False, help_text="", verbose_name="Is teacher"
            ),
        ),
    ]