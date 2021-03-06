# Generated by Django 2.1.5 on 2019-02-09 20:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("core", "0004_auto_20190209_2011")]

    operations = [
        migrations.CreateModel(
            name="FoodNutrition",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("desc", models.CharField(max_length=60)),
                ("value", models.DecimalField(decimal_places=3, max_digits=10)),
                ("units", models.CharField(max_length=7)),
                (
                    "min_val",
                    models.DecimalField(
                        blank=True, decimal_places=3, max_digits=10, null=True
                    ),
                ),
                (
                    "max_val",
                    models.DecimalField(
                        blank=True, decimal_places=3, max_digits=10, null=True
                    ),
                ),
                ("tagname", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "food",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="nutrition",
                        to="core.Food",
                    ),
                ),
            ],
        )
    ]
