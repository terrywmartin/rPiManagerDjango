# Generated by Django 4.1 on 2022-08-12 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rpi", "0003_alter_raspberrypi_checked_in_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="raspberrypi",
            name="ip_address",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
