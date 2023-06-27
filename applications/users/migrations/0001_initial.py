# Generated by Django 4.2.2 on 2023-06-27 05:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("email", models.EmailField(max_length=255, unique=True)),
                (
                    "username",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="username"
                    ),
                ),
                (
                    "is_teacher",
                    models.BooleanField(
                        default=False, help_text="", verbose_name="Is teacher"
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(auto_now_add=True, verbose_name="date joined"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=255, verbose_name="first name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=255, verbose_name="last name"),
                ),
                (
                    "userpic",
                    models.ImageField(
                        upload_to="userpics/%Y/%m/%d", verbose_name="User picture"
                    ),
                ),
                ("country", models.CharField(max_length=100, verbose_name="country")),
                (
                    "phone",
                    models.CharField(
                        max_length=14, unique=True, verbose_name="phone number"
                    ),
                ),
                ("city", models.CharField(max_length=255, verbose_name="city")),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]