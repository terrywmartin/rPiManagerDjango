# Generated by Django 4.1 on 2022-08-11 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rpi", "0002_rename_model_raspberrypimodel_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="raspberrypi",
            name="checked_in",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="raspberrypi",
            name="date_deployed",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
