# Generated by Django 4.2.2 on 2023-06-29 17:54
import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AbstractModuleBlock",
            fields=[
                (
                    "id",
                    models.UUIDField(editable=False, primary_key=True, serialize=False),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("text", models.TextField()),
                ("video", models.FileField(upload_to="videos/%Y/%m/%d")),
                ("audio", models.FileField(upload_to="audios/%Y/%m/%d")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="TestQuestion",
            fields=[
                (
                    "id",
                    models.UUIDField(editable=False, primary_key=True, serialize=False),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("question_body", models.TextField()),
            ],
            options={
                "verbose_name": "Question",
                "verbose_name_plural": "Questions",
            },
        ),
        migrations.CreateModel(
            name="Test",
            fields=[
                (
                    "abstractmoduleblock_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="module_parts.abstractmoduleblock",
                    ),
                ),
                (
                    "module",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="module_tests",
                        to="courses.programmodule",
                    ),
                ),
            ],
            options={
                "verbose_name": "Test",
                "verbose_name_plural": "Tests",
            },
            bases=("module_parts.abstractmoduleblock",),
        ),
        migrations.CreateModel(
            name="TestAnswer",
            fields=[
                (
                    "id",
                    models.UUIDField(editable=False, primary_key=True, serialize=False),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("text", models.TextField()),
                ("is_right", models.BooleanField()),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="answers",
                        to="module_parts.testquestion",
                    ),
                ),
            ],
            options={
                "verbose_name": "Answer",
                "verbose_name_plural": "Answers",
            },
        ),
        migrations.AddField(
            model_name="testquestion",
            name="test",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="questions",
                to="module_parts.test",
            ),
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "abstractmoduleblock_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="module_parts.abstractmoduleblock",
                    ),
                ),
                (
                    "module",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="module_tasks",
                        to="courses.programmodule",
                    ),
                ),
            ],
            options={
                "verbose_name": "Task",
                "verbose_name_plural": "Tasks",
            },
            bases=("module_parts.abstractmoduleblock",),
        ),
        migrations.CreateModel(
            name="Lesson",
            fields=[
                (
                    "abstractmoduleblock_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="module_parts.abstractmoduleblock",
                    ),
                ),
                (
                    "module",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="module_lessons",
                        to="courses.programmodule",
                    ),
                ),
            ],
            options={
                "verbose_name": "Lesson",
                "verbose_name_plural": "Lessons",
            },
            bases=("module_parts.abstractmoduleblock",),
        ),
    ]
