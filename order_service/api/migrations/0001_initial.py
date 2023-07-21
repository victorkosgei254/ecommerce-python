# Generated by Django 4.2.3 on 2023-07-21 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("product_id", models.CharField(max_length=255)),
                ("title", models.CharField(max_length=255)),
                ("cart_id", models.CharField(max_length=255)),
            ],
        ),
    ]
