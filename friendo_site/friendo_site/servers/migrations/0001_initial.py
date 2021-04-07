# Generated by Django 3.1.7 on 2021-04-07 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Server",
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
                ("server_id", models.IntegerField()),
                ("dogeboard_id", models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]