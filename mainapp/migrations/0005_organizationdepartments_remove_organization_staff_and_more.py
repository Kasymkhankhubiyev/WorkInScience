# Generated by Django 4.1.7 on 2023-04-02 08:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0004_alter_useradditionaldata_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrganizationDepartments",
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
            ],
        ),
        migrations.RemoveField(
            model_name="organization",
            name="staff",
        ),
        migrations.AddField(
            model_name="useradditionaldata",
            name="education",
            field=models.CharField(default="Среднее.", max_length=64),
        ),
        migrations.AddField(
            model_name="useradditionaldata",
            name="scientific_degree",
            field=models.CharField(
                blank=True, default="Без степени", max_length=64, null=True
            ),
        ),
        migrations.CreateModel(
            name="UserPosts",
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
                ("title", models.CharField(default="Заголовок", max_length=64)),
                (
                    "short_description",
                    models.TextField(blank=True, default="Без описания", null=True),
                ),
                ("body", models.TextField(blank=True)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("None", "Выберите тип публикации"),
                            ("v", "Вакансия"),
                            ("n", "Новость"),
                        ],
                        max_length=64,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserInterestSphere",
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
                ("sphere_name", models.CharField(max_length=128)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrganizationStaff",
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
                ("subdep", models.IntegerField(blank=True, default=0, null=True)),
                ("position", models.CharField(max_length=64)),
                ("access_level", models.IntegerField(default=0)),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="mainapp.organization",
                    ),
                ),
                ("user", models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]