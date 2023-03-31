# Generated by Django 4.1.7 on 2023-03-31 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Organization",
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
                ("name", models.CharField(max_length=64)),
                ("bin", models.CharField(max_length=64)),
                ("email_block", models.CharField(max_length=64)),
                (
                    "organization_type",
                    models.CharField(
                        choices=[
                            ("None", "Выберите тип организации"),
                            ("c", "Компания"),
                            ("i", "Институт"),
                            ("u", "Университет"),
                        ],
                        max_length=64,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="user",
            name="position",
            field=models.CharField(
                blank=64,
                choices=[("m", "Менеджер"), ("s", "Студент")],
                default="Студент",
                max_length=64,
            ),
        ),
    ]
