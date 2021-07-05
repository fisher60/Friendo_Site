# Generated by Django 3.1.3 on 2020-11-25 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_user_discord_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="avatar",
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name="user",
            name="discord_discriminator",
            field=models.CharField(default=None, max_length=4),
        ),
        migrations.AddField(
            model_name="user",
            name="discord_username",
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name="user",
            name="discord_id",
            field=models.BigIntegerField(default=None),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_login",
            field=models.DateTimeField(default=None),
        ),
    ]